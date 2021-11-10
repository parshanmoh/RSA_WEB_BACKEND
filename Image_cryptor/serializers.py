# from rest_framework.serializers import Serializer, FileField, ListField
from rest_framework import serializers
from .models import ImageFile, keyGenrator,Decrypt


# Serializers define the API representation.


class ImageFileSerializer(serializers.ModelSerializer):

    class Meta:

        model = ImageFile

        fields = '__all__'



class keyGenratorSerializer(serializers.ModelSerializer):

    class Meta:

        model = keyGenrator

        fields = '__all__'


class DecryptSerializer(serializers.ModelSerializer):

    class Meta:

        model = Decrypt

        fields = '__all__'

