from django.db import models
import datetime
# Create your models here.
class student(models.Model):
    image=models.ImageField(upload_to="profile_images")
    fname=models.CharField(max_length=32)
    lname=models.CharField(max_length=32)
    emailid=models.EmailField()
    phone=models.BigIntegerField()
    qualification=models.CharField(max_length=30)
    location=models.CharField(max_length=50)
    description=models.TextField()
    date=models.DateField(default=datetime.date.today)
