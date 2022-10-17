from rest_framework import serializers
from BookApp.models import Users,Ebook


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= Users
        fields=('Username','Password')


class EbookSerializer(serializers.ModelSerializer):
    class Meta:
        model= Ebook
        fields=('Title','Auther','Genre','Rating','Favourite')