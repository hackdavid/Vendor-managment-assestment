from django.db import models
import uuid
from datetime import datetime
# Create your models here.

class OrderStatus:
    PENDING = 'pending'
    COMPLETED = 'completed'
    CANCELED = 'canceled'


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        abstract = True
class VenderProfile(TimeStampedModel):
    name = models.CharField(max_length=100)
    contact_details = models.TextField(null=True)
    address = models.TextField()
    vender_code = models.CharField(default=uuid.uuid4().hex[:6].upper(),max_length=30)  #can be use any format like combitionation vender_name_date_of_created_total_number_of_vender
    on_time_delivery_rate = models.FloatField(default=0,null=True)
    quality_rating_avg = models.FloatField(default=0,null=True)
    average_response_time = models.FloatField(default=0,null=True)
    fulfillment_rate = models.FloatField(default=0,null=True)

    def __str__(self) -> str:
        return str(self.name)


class PurchaseOrder(TimeStampedModel):
    STATUS_CHOICES = (
        (OrderStatus.PENDING,OrderStatus.PENDING),
        (OrderStatus.COMPLETED,OrderStatus.COMPLETED),
        (OrderStatus.CANCELED,OrderStatus.CANCELED),
    )
    po_number = models.CharField(default=uuid.uuid4(),max_length=50)
    vender = models.ForeignKey(VenderProfile,on_delete=models.PROTECT)
    order_date = models.DateTimeField(auto_now=True)
    delivery_date = models.DateTimeField(null=True)
    items = models.JSONField(null=True)
    quantity = models.IntegerField(null=True)
    status = models.CharField(default=OrderStatus.PENDING,max_length=20,choices=STATUS_CHOICES)
    order_completed_date = models.DateTimeField(null=True)
    quality_rating = models.FloatField(default=0,null=True)
    issue_date = models.DateTimeField(auto_now=True,null=True)
    acknowledgment_date = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        # adding a one extra filed 'order_completed_date' and update this date when status becuase completed
        if self.status == OrderStatus.COMPLETED:
            self.order_completed_date = datetime.now()
        super(PurchaseOrder, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return str(self.po_number)


class HistoricalPerformance(TimeStampedModel):
    vender = models.ForeignKey(VenderProfile,on_delete=models.PROTECT)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

