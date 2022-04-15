
from django.db import models

# Create your models here.
class Adds(models.Model):
    addId=models.AutoField
    addName=models.CharField(max_length=50,default="")
    petCatgory=models.CharField(max_length=50,default="")
    addDescription=models.CharField(max_length=300,default="")
    userId=models.IntegerField(max_length=20,default=0)
    price=models.IntegerField(default=0)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")
    
    def __str__(self):
        return self.addName