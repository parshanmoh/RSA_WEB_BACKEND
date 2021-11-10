from django.db import models

# Create your models here. for file fields

class ImageFile(models.Model):

    public_key = models.FileField(upload_to='public_keys',name='public_key')

    image = models.FileField(name='image')



class Decrypt(models.Model):

    private_key = models.FileField(upload_to='private_keys', name='private_key')

    image = models.FileField(name='image')




class keyGenrator(models.Model):

    private_key = models.FileField(upload_to='keys',db_index=True)

    public = models.FileField(upload_to='key',db_index=True)


