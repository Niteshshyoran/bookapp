from tokenize import Comment
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Author,Books,Country



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    # def create(self, validated_data):
    #         return Comment.objects.create(**validated_data)

    
    # def update(self, instance, validated_data):
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.created = validated_data.get('created', instance.created)
    #     instance.save()
    #     return instance
    

class AuthorSerializer(serializers.ModelSerializer):
     class Meta:
          model = Author
          fields = '__all__'



class BookSerializer(serializers.ModelSerializer):
     class Meta:
          model = Books
          fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
     class Meta:
          model = Country
          fields = '__all__'
