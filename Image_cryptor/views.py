from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.http.response import HttpResponse
import mimetypes
from .RSA_DECFILE import DencryptFile
from .serializers import ImageFileSerializer, keyGenratorSerializer, DecryptSerializer
from .models import ImageFile, Decrypt
from Crypto.PublicKey import RSA
from .RSA_KEYGEN_FILE import KeyGen
from .RSA_ENCFILE import EncryptFile
from django.conf import settings
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive



# function for uploading files in Google Drive

def GoogleUploadForKeys(nn):

    g_login = GoogleAuth()

    g_login.LocalWebserverAuth()

    drive = GoogleDrive(g_login)

    with open(nn, "r") as file:

        file_drive = drive.CreateFile({'title': os.path.basename(nn)})

        file_drive.SetContentString(file.read())

        file_drive.Upload()





class keyGenView(ViewSet):

    counter = 1

    serializer_class = keyGenratorSerializer

    # function for generating private keys and public keys then upload them in Google Drive

    def list(self,request):

        new_key = RSA.generate(4096, e=65537)

        private_key_pem = new_key.exportKey("PEM")

        public_key_pem = new_key.publickey().exportKey("PEM")

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + settings.MEDIA_URL

        keygenerator = KeyGen(pk = private_key_pem , pbk = public_key_pem , id = self.counter , path = BASE_DIR)

        private_key_generate=keygenerator.make_private_key(private_key_pem)

        GoogleUploadForKeys(private_key_generate)

        public_key_generate=keygenerator.make_public_key(public_key_pem)

        GoogleUploadForKeys(public_key_generate)

        return Response("ok")





class UploadViewSet(ViewSet):

    serializer_class = ImageFileSerializer

    def list(self, request):

        return Response("GET API")

    #  function for files which are going to add the media repository

    def create(self, request):

        data = request.data

        serializer = ImageFileSerializer(data=data)

        if serializer.is_valid():

            images = ImageFile.objects.all()

            for image in images:

                if image == data['image']:

                    response = 'reapeted file'

                    return Response(response)

            serializer.save()

            # path the files in media/image

            data = serializer.data

            file_path = data['image']

            file_name = os.path.basename(data['image'])

            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + file_path

            pbk = data['public_key']

            # call encryption class then function with path of the file and public key to encrypt. then upload it in Google Drive

            pbk_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + pbk

            enc_var = EncryptFile(pbk=pbk_path,file_path=BASE_DIR,file_name=file_name)

            enc_file = enc_var.crypting_file()

            GoogleUploadForKeys(enc_file)

            return Response("ok")

        else:

            return Response('its not ok!')




class DecryptViewSet(ViewSet):

    serializer_class = DecryptSerializer

    def list(self, request):

        return Response("GET API")

    def create(self, request):

        data = request.data

        serializer = DecryptSerializer(data=data)

        if serializer.is_valid():

            images = Decrypt.objects.all()

            for image in images:

                if image == data['image']:

                    response = 'reapeted file'

                    return Response(response)

            serializer.save()

            data = serializer.data

            file_path = data['image']

            file_name = os.path.basename(data['image'])

            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + file_path

            prk = data['private_key']

            prk_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + prk

            dec_var = DencryptFile(prk=prk_path,file_path=BASE_DIR,file_name=file_name)

            dec_file = dec_var.dencrypting_file()

            GoogleUploadForKeys(dec_file)

            return Response("ok")

        else:

            return Response('its not ok!')
