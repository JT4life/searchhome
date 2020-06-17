from django.db import models
from django.utils import timezone

class SendMessage(models.Model):
    email = models.CharField(max_length=70)
    message = models.TextField()

    def __str__(self):
        return self.email

class Agent(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    images = models.ImageField(upload_to='pic')

    def __str__(self):
        return self.name

class Property(models.Model):
    name = models.CharField(max_length=100)
    type_home_choices = (('house','house'),('apartment','apartment'))
    housing = models.CharField(max_length=30, choices=type_home_choices, default='house')
    location = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    choices = (('rent','rent'),('sale','sale'))
    purpose = models.CharField(max_length=30,choices=choices,default='rent')
    details = models.TextField()
    images = models.ImageField(upload_to='pic')
    created = models.DateTimeField(default=timezone.now)
    agent_name = models.ForeignKey(Agent, on_delete=models.CASCADE)

    def __str__(self):
        return self.name