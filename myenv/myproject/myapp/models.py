from django.db import models

# Create your models here.
class Emp(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    salary = models.IntegerField()
    def __str__(self):
        return f'{self.firstname} {self.lastname}'


#----- Signup form models----

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

#blog post

class Blogpost(models.Model):
    title = models.CharField(max_length=200)
    post = models.CharField(max_length=500, default='')
    thumbnail = models.ImageField(upload_to='images/', null=True, blank=True)
    def __str__(self):
        return self.title
    
    # python manage.py makemigrations
    # python manage.py migrate

