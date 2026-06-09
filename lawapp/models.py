from django.db import models


# Create your models here.


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.TextField(max_length=500)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = "contact"


class Notifications(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Notifications"
