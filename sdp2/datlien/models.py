from django.db import models

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class CentralHub(models.Model):
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    city = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    established_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.city} - {self.state}"

class Hub(models.Model):
    central_hub = models.ForeignKey(CentralHub,on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    established_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.city