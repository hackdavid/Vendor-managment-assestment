from vender.models import OrderStatus
from django.db.models import F
from django.db.models import Avg

class PerformanceMatrixUtils:
    '''
    Note i am passing queryset and using filter based on logic
    and each queryset is related to vender so no need to make filter on vender here

    '''
    @classmethod
    def get_time_delivery_rate(cls,queryset):
        total_completed_order = len(queryset.filter(status=OrderStatus.COMPLETED))
        on_time_order_completed = len(queryset.filter(order_completed_date__lte=F('delivery_date')))
        if total_completed_order:
            return float(on_time_order_completed/total_completed_order)
        else:
            return 0
        
    @classmethod
    def quality_rating_average(cls,queryset):
        avg = queryset.filter(status=OrderStatus.COMPLETED).aggregate(Avg('quality_rating'))
        print('avarage rating ',avg)
        return avg
    
    @classmethod
    def average_response_time(cls,queryset):
        all_order = len(queryset.all())
        difff_time = sum([float(item.issue_date - item.acknowledgment_date) for item in queryset if item.acknowledgment_date])
        if all_order:
            return float(difff_time/all_order)
        else:
            return 0

    @classmethod
    def fulfilment_rate(cls,queryset):
        total_order = len(queryset.all())
        completed_order = len(queryset.filter(status=OrderStatus.COMPLETED))
        if total_order:
            return float(completed_order/total_order)
        else:
            return 0

