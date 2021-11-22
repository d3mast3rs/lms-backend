from rest_framework import serializers
from .models import User, Book, Author, Genre, Publisher, LibraryCard
from django.contrib.auth.models import update_last_login
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.settings import api_settings


class UserSerializer(serializers.ModelSerializer):
    dob = serializers.DateField(format='%d/%m/%Y', input_formats=('%d/%m/%Y',))

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            type=validated_data['type'],
            dob=validated_data['dob'],
            phone = validated_data['phone'],
            gender = validated_data['gender'],
            password = make_password(validated_data['password']))
        user.save()
        return user


class UserLoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super().validate(attrs)
        
        data.pop('access')
        data.pop('refresh')

        refresh = self.get_token(self.user)

        data['id'] = self.user.id
        data['first_name'] = self.user.first_name
        data['last_name'] = self.user.last_name
        data['email'] = self.user.email
        data['type'] = self.user.type
        data['dob'] = self.user.dob
        data['phone'] = self.user.phone
        data['gender'] = self.user.gender
        data['token'] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data

class BookSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Book
        ordering = ['-id']
        extra_kwargs = {'authors': {'required': False}, 'genres': {'required': False}, 'users_who_issued': {'required': False}}
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        ordering = ['-id']
        model = Author
        extra_kwargs = {'books': {'required': False}}
        fields = ('id', 'first_name', 'last_name', 'books')

class GenreSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        ordering = ['-id']
        model = Genre
        extra_kwargs = {'books': {'required': False}}
        fields = ('id', 'genre', 'books')

class PublisherSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        ordering = ['-id']
        model = Publisher
        extra_kwargs = {'books': {'required': False}}
        fields = ('id', 'publisher', 'books')

class LibraryCardSerializer(serializers.ModelSerializer):
    books_issued = BookSerializer(many=True, read_only=True)

    class Meta:
        model = LibraryCard
        ordering = ['-id']
        extra_kwargs = {'books_issued': {'required': False}}
        fields = ('user_id', 'first_name', 'last_name', 'books_issued')