from django.db import models
from django.contrib.auth import User
# Create your models here.


class Author(models.Model):
    name = models.CharField( max_length=50)
    birthday = models.DateField()
    biography = models.CharField( max_length=500,blank=True,default=None)
    def __str__(self):
        return self.name


class Books(models.Model):
    title = models.CharField(max_length=40)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateTimeField( auto_now=False, auto_now_add=False)
    isbn = models.TextField(max_length=20)
    price = models.DecimalField(max_digits=100000,decimal_places=4)
    stock = models.IntegerField()
    def __str__(self) :
        return self.title



class Country(models.Model):
    name = models.CharField( max_length=50 , unique=True)
    code = models.CharField(max_length=64, unique=True)