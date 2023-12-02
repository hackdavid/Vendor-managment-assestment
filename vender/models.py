from django.db import models
import uuid

# Create your models here.
class VenderProfile(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15) # taking charfiled becuse contanct have +91 contry code
    details = models.CharField(max_length=300)
    address = models.CharField(max_length=150)
    vender_code = models.CharField(default=uuid.uuid4().hex[:6].upper(),max_length=30)  #can be use any format like combitionation vender_name_date_of_created_total_number_of_vender

