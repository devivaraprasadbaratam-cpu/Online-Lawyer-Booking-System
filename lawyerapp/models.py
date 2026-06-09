from django.db import models

# Create your models here.


class Lawyer(models.Model):
    suffix = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    city = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.TextField()
    current = models.TextField()
    image = models.ImageField(upload_to='images/')
    status = models.CharField(max_length=100,default="on hold")

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = "lawyer"


class Services(models.Model):
    email = models.EmailField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    images = models.FileField()
    cost = models.BigIntegerField()

    class Meta:
        db_table = "Services"

