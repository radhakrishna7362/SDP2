from django.db import models
from datlien.models import DeliveryBoy, Hub
from datetime import datetime
from django_random_id_model import RandomIDModel

# Create your models here.
class Delivery(RandomIDModel):
    user = models.CharField(max_length=100)
    source = models.ForeignKey(Hub,on_delete=models.CASCADE,related_name='+')
    destination = models.ForeignKey(Hub,on_delete=models.CASCADE,related_name='+')
    is_approved = models.BooleanField(default=False)
    is_picked = models.BooleanField(default=False)
    is_shipped = models.BooleanField(default=False)
    is_transit = models.BooleanField(default=False)
    is_received = models.BooleanField(default=False)
    is_assigned = models.BooleanField(default=False)
    out_for_delivery = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.id}"

class DeliveryAgent(RandomIDModel):
    delivery = models.ForeignKey(Delivery,on_delete=models.CASCADE,related_name='+',verbose_name="Package Id")
    delivery_boy = models.ForeignKey(DeliveryBoy,on_delete=models.CASCADE,related_name='+')
    is_delivered=models.BooleanField(default=False)