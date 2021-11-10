import os
from os.path import join




class KeyGen():

    def __init__(self,pk,pbk,id,path):

        self.pk = pk

        self.pbk = pbk

        self.id = id

        self.path = path

        print('path: ',path)

    #  function to create private keys as PEM file

    def make_private_key(self,pk):

        fd = open(join(self.path, "private_key.pem"), "wb")

        fd.write(pk)

        fd.close()

        return self.path + 'private_key.pem'

    #  function to create public keys as PEM file

    def make_public_key(self,pbk):

        fd = open(join(self.path, "public_key.pem"), "wb")

        fd.write(pbk)

        fd.close()

        return self.path + 'public_key.pem'


