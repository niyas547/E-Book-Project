from rest_framework import serializers
from api.models import Genre,Books,Review
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class GenreSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Genre
        fields="__all__"

class BookSerializer(serializers.ModelSerializer):
    genre=GenreSerializer(read_only=True)
    id=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Books
        fields="__all__"
    def create(self, validated_data):
        user=self.context.get("user")
        genre=self.context.get("genre")
        return Books.objects.create(**validated_data,user=user,genre=genre)

class ReviewSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    book_name=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Review
        fields="__all__"
    def create(self, validated_data):
        user=self.context.get("user")
        book_name=self.context.get("book_name")
        return Review.objects.create(**validated_data,user=user,book_name=book_name)


