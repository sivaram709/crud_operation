from rest_framework import serializers
from .models import *

class Contactserializers(serializers.ModelSerializer):


    class Meta:
        model=ContactModel
        fields="__all__"