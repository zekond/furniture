from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

def upload_path(self, filename):
    return 'uploads/media/%s/' % filename

class Category(models.Model):
    image = models.ImageField(upload_to=upload_path, default='/media/image')
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

class Youth(models.Model):
    image = models.ImageField(upload_to=upload_path, default='/media/image')
    name = models.CharField(max_length=20)
    sumary = models.CharField(max_length=500)
    status = models.BooleanField(default=True)
    price = models.IntegerField()
    youth = models.ForeignKey('Category')

    def __unicode__(self):
        return self.name

class Mattress(models.Model):
    image = models.ImageField(upload_to=upload_path, default='/media/image')
    name = models.CharField(max_length=20)
    sumary = models.CharField(max_length=500)
    status = models.BooleanField(default=True)
    price = models.IntegerField()

    def __unicode__(self):
        return self.name

class Bedroom(models.Model):
    image = models.ImageField(upload_to=upload_path, default='/media/image')
    name = models.CharField(max_length=20)
    sumary = models.CharField(max_length=500)
    status = models.BooleanField(default=True)
    price = models.IntegerField()

    def __unicode__(self):
        return self.name

class Diningroom(models.Model):
    image = models.ImageField(upload_to=upload_path, default='/media/image')
    name = models.CharField(max_length=20)
    sumary = models.CharField(max_length=500)
    status = models.BooleanField(default=True)
    price = models.IntegerField()
    def __unicode__(self):
        return self.name

class Livingroom(models.Model):
    image = models.ImageField(upload_to=upload_path, default='/media/image')
    name = models.CharField(max_length=20)
    sumary = models.CharField(max_length=500)
    status = models.BooleanField(default=True)
    price = models.IntegerField()
    def __unicode__(self):
        return self.name

class Home(models.Model):
    image = models.ImageField(upload_to=upload_path, default='/media/image')
    image2 = models.ImageField(upload_to=upload_path, default='/media/image')
    name = models.CharField(max_length=20)
    sumary = models.CharField(max_length=500)
    status = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name