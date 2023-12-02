from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from vender.models import (
    VenderProfile,
)

from vender.serializer import (
    VenderProfileSerializer
)
# Create your views here.
def home(request):
    return HttpResponse('Welcome to vender managament system')


# 1. Vendor Profile Management:
class VenderProfileViewset(GenericViewSet):
    '''
    ● Model Design: Create a model to store vendor information including name, contact
    details, address, and a unique vendor code.
    ● API Endpoints:
    ● POST /api/vendors/: Create a new vendor.
    ● GET /api/vendors/: List all vendors.
    ● GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.
    ● PUT /api/vendors/{vendor_id}/: Update a vendor's details.
    ● DELETE /api/vendors/{vendor_id}/: Delete a vendor.
    
    '''
    queryset = VenderProfile.objects.all()
    serializer_class = VenderProfileSerializer

    def create(self,request, *args, **kwargs):
        # POST /api/vendors/: Create a new vendor.
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self,request):
        # GET /api/vendors/: List all vendors.
        serialized_data = self.get_serializer(self.queryset,many=True)
        return Response(serialized_data.data)

    def retrieve(self,request,pk=None):
        # GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.
        vender_info = get_object_or_404(self.queryset, pk=pk)
        serializer = self.get_serializer(vender_info)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        instance = get_object_or_404(self.queryset,pk=int(pk))
        if instance:
            serilizer = self.get_serializer(instance,data=request.data,partial=True)
            serilizer.is_valid(raise_exception=True)
            serilizer.save()
            return Response(serilizer.data)

    # def partial_update(self, request, *args, **kwargs):
    #     # PUT /api/vendors/{vendor_id}/: Update a vendor's details.
    #     instance = self.queryset.get(pk=kwargs.get('pk'))
    #     serializer = self.get_serializer(instance, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)

    def destroy(self,request,pk=None):
        #DELETE /api/vendors/{vendor_id}/: Delete a vendor.
        vender_info = get_object_or_404(self.queryset, pk=int(pk))
        if vender_info:
            vender_info.delete()
        return Response('Vender is delete successfully........')