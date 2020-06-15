from django.db import models
from django.utils import timezone

class Property(models.Model):
    name = models.CharField(max_length=100)
    type_home_choices = (('house','house'),('apartment','apartment'))
    housing = models.CharField(max_length=30, choices=type_home_choices, default='house')
    location = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    price = models.IntegerField()
    choices = (('rent','rent'),('sale','sale'))
    purpose = models.CharField(max_length=30,choices=choices,default='rent')
    details = models.TextField()
    images = models.ImageField(upload_to='pic')
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class SendMessage(models.Model):
    email = models.CharField(max_length=70)
    message = models.TextField()

    def __str__(self):
        return self.email