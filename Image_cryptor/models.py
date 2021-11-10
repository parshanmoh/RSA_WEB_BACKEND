from django.db import models

# Create your models here.
class ImageFile(models.Model):

    # upload_to = 'images', for below in ()
    public_key = models.FileField(upload_to='public_keys',name='public_key')
    image = models.FileField(name='image')



    # public_key = models.CharField(max_length=4000,default="no key")


class Decrypt(models.Model):
    # upload_to = 'images', for below in ()
    private_key = models.FileField(upload_to='private_keys', name='private_key')
    image = models.FileField(name='image')

    # public_key = models.CharField(max_length=4000,default="no key")


class keyGenrator(models.Model):

    private_key = models.FileField(upload_to='keys',db_index=True)

    public = models.FileField(upload_to='key',db_index=True)


