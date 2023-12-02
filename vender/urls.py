from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from vender.views import (
    VenderProfileViewset,
    home,
)

router = routers.DefaultRouter()
router.register(r'venders',VenderProfileViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('api/', include(router.urls)),
]
