from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import zlib
from os.path import join
import os
from django.conf import settings



class DencryptFile:

    def __init__(self,prk,file_path, file_name):

        self.prk_file_path = prk

        self.file_path = file_path

        self.file_name = file_name


    #Our Decryption Function

    def decrypt_blob(self,encrypted_blob, private_key):

        #Import the Private Key and use for decryption using PKCS1_OAEP

        rsakey = RSA.importKey(private_key)

        rsakey = PKCS1_OAEP.new(rsakey)

        #Base 64 decode the data

        encrypted_blob = base64.b64decode(encrypted_blob)

        #In determining the chunk size, determine the private key length used in bytes.
        #The data will be in decrypted in chunks

        chunk_size = 512

        offset = 0

        decrypted =b""

        #keep loop going as long as we have chunks to decrypt

        while offset < len(encrypted_blob):

            #The chunk

            chunk = encrypted_blob[offset: offset + chunk_size]

            #Append the decrypted chunk to the overall decrypted file

            decrypted += rsakey.decrypt(chunk)

            #Increase the offset by chunk size

            offset += chunk_size

        #return the decompressed decrypted data

        return zlib.decompress(decrypted)


    def dencrypting_file(self):

        #Use the private key for decryption

        fd = open(self.prk_file_path, "rb")

        self.prk = fd.read()

        fd.close()

        #Our candidate file to be decrypted

        fd = open(self.file_path, "rb")

        self.ddencrypted_blob = fd.read()

        fd.close()

        dencrypted_blob = self.decrypt_blob(self.ddencrypted_blob, self.prk)

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + settings.MEDIA_URL

        fd = open(join(BASE_DIR, "dec" + self.file_name), "wb")

        fd.write(dencrypted_blob)

        fd.close()


        return join(BASE_DIR, "dec" + self.file_name)
