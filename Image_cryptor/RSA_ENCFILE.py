from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import zlib
import base64
from os.path import join
import os
from django.conf import settings

#Our Encryption Function

class EncryptFile:

    def __init__(self,pbk,file_path, file_name):

        self.pbk_file_path = pbk

        self.file_path = file_path

        self.file_name = file_name


    def encrypt_blob(self,blob,public_key):

    #Import the Public Key and use for encryption using PKCS1_OAEP


        rsa_key = RSA.importKey(public_key)

        rsa_key = PKCS1_OAEP.new(rsa_key)

    #compress the data first

        blob = zlib.compress(blob)

    #In determining the chunk size, determine the private key length used in bytes
    #and subtract 42 bytes (when using PKCS1_OAEP). The data will be in encrypted
    #in chunks

        chunk_size = 470

        offset = 0

        end_loop = False

        encrypted =b""

        while not end_loop:

        #The chunk

            chunk = blob[offset:offset + chunk_size]

        #If the data chunk is less then the chunk size, then we need to add
        #padding with " ". This indicates the we reached the end of the file
        #so we end loop here

            if len(chunk) % chunk_size != 0:

                end_loop = True

                chunk +=b" " * (chunk_size - len(chunk))

        #Append the encrypted chunk to the overall encrypted file

            encrypted += rsa_key.encrypt(chunk)

        #Increase the offset by chunk size

            offset += chunk_size

    #Base 64 encode the encrypted file

        return base64.b64encode(encrypted)

#Use the public key for encryption

    def crypting_file(self):

        fd = open(self.pbk_file_path, "rb")

        self.pbk = fd.read()

        fd.close()

#Our candidate file to be encrypted

        fd = open(self.file_path, "rb")

        self.unencrypted_blob = fd.read()

        fd.close()

        encrypted_blob = self.encrypt_blob(self.unencrypted_blob,self.pbk)


        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + settings.MEDIA_URL

        fd = open(join(BASE_DIR, "enc"+self.file_name), "wb")

        fd.write(encrypted_blob)

        fd.close()

        return join(BASE_DIR,"enc"+self.file_name)
