from django.db.models.signals import post_save
from django.dispatch import receiver
from vender.models import PurchaseOrder, OrderStatus
from datetime import datetime
from vender.utils import PerformanceMatrixUtils

@receiver(post_save, sender=PurchaseOrder)
def user_created(sender, instance, created, **kwargs):
    if created:
        vender = instance.vender
        queryset = PurchaseOrder.objects.filter(vender=vender)
        if instance.acknowledgment_date:
            vender.average_response_time = PerformanceMatrixUtils.average_response_time(queryset=queryset)
        if instance.status == OrderStatus.COMPLETED:
            vender.on_time_delivery_rate = PerformanceMatrixUtils.get_time_delivery_rate(queryset=queryset)
            vender.quality_rating_avg = PerformanceMatrixUtils.quality_rating_average(queryset=queryset)
            vender.fulfillment_rate = PerformanceMatrixUtils.fulfilment_rate(queryset=queryset)
        vender.save()
        print(f'Performance Matrix is  updated for vender {vender.name}')