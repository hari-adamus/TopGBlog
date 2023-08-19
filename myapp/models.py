from django.db import models
from datetime import datetime

# Create your models here.

class post(models.Model):
    title=models.CharField(max_length=150)
    body=models.CharField(max_length=1000000)
    #img=models.ImageField(null=True, blank=True,upload_to='img_files/')
    date_made=models.DateTimeField(default=datetime.now,blank=True)
    comments=models.CharField(max_length=1000000000)
    post_username=models.CharField(max_length=100)
    

