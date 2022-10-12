from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Genre(models.Model):
    genre_name=models.CharField(max_length=120)
    def __str__(self):
        return self.genre_name

class Books(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book_title=models.CharField(max_length=120)
    genre=models.ForeignKey(Genre,on_delete=models.CASCADE,null=True)
    author=models.CharField(max_length=120)
    rating=models.FloatField(null=True,default=3)
    favorite=models.BooleanField(default=False)
    def __str__(self):
        return self.book_title
class Review(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book_name=models.ForeignKey(Books,on_delete=models.CASCADE)
    description=models.CharField(max_length=200)
    def __str__(self):
        return self.description

