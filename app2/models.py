from distutils.command.upload import upload
from random import choice
from tkinter import N
from django.db import models


class Employee(models.Model):
      eid = models.CharField(max_length=20 )
      ename = models.CharField(max_length=100)
      econtact = models.CharField(max_length=15)
      class Meta:
        db_table ="employee"


class Signup(models.Model):
      gen=[('male','male'),('female','female'),('others','others')]
      username=models.CharField(max_length=20)
      email=models.EmailField(max_length=50)
      mnumber=models.CharField(max_length=10)
      gender=models.CharField(max_length=7,choices=gen)
      password_1=models.CharField(max_length=20)
      password_2=models.CharField(max_length=20)
      class Meta:
            db_table="usersignup"
           

class products(models.Model):
      id_num=models.IntegerField(default=1)
      device_name=models.CharField(max_length=50)
      device_model=models.CharField(max_length=100)
      device_dis=models.TextField(max_length=250)
      price=models.CharField(max_length=10)
      addimage=models.ImageField(upload_to="images/")
      class Meata:
            db_table="products"

class mobile(models.Model):
      mobile_company=models.CharField(max_length=16)
      mobilename=models.CharField(max_length=20)
      price=models.IntegerField()
      description=models.TextField()
      image=models.ImageField(upload_to="mobileimages/")

      class Meata:
            db_table="mobile"


class oneplus(models.Model):
      name=models.CharField(max_length=20,default="oneplus")
      modelname=models.CharField(max_length=25)
      price=models.IntegerField(default=None)
      discription=models.TextField()
      image=models.ImageField(upload_to="oneplusimages")
      class Meta:
            db_table="oneplusmob."

class redmi(models.Model):
      name = models.CharField(max_length=20, default="redmi")
      modelname = models.CharField(max_length=25)
      price = models.IntegerField(default=None)
      discription = models.TextField()
      image = models.ImageField(upload_to="redmimages")
      class Meta:
            db_table="redmimob"
