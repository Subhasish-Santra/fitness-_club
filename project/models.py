from django.db import models

class logdata(models.Model):
    name = models.CharField(max_length=100)
    password = models.IntegerField()
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    age = models.IntegerField()
    class Meta:
        db_table = 'logdata'

class Registration(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name
