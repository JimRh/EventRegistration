from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):

    title=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    date=models.DateField()
    time=models.TimeField()
    location=models.CharField(max_length=200)
    slots=models.IntegerField()
    event_creator=models.ForeignKey(User,on_delete=models.CASCADE,related_name='creator')

class Registered_events(models.Model):
    
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    participants=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)