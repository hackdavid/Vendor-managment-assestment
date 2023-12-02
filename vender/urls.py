from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from vender.views import (
    VenderProfileViewset,
    home,
    PurchaseOrderViwset,
    TokenGeneration
)

router = routers.DefaultRouter()
router.register(r'venders',VenderProfileViewset)
router.register(r'purchase_orders',PurchaseOrderViwset)
router.register(r'token',TokenGeneration)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('api/', include(router.urls)),
]
