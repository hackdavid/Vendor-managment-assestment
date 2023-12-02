from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from datetime import datetime
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User


from vender.models import (
    VenderProfile,
    PurchaseOrder,
    HistoricalPerformance
)

from vender.serializer import (
    VenderProfileSerializer,
    PurchaseOrderSerializer,
    HistoricalPerformanceSerializer,
    UserSerializer
)
# Create your views here.
def home(request):
    return HttpResponse('Welcome to vender managament system')

def generate_token(request):
    user = User.objects.get(username='your_username')
    token, created = Token.objects.get_or_create(user=user)


class TokenGeneration(GenericViewSet):
    '''
    This section is used to generate new token or get token based on email
    so if you want to access the api end-point please generate token first and then use this token 
    with header 

    'Authorization: Token 9054f7aa9305e012b3c2300408c3dfdf390fcddf'
    
    '''

    queryset = User.objects.all()
    serializer_class = UserSerializer
    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        user,_created = User.objects.get_or_create(email=email)
        token,created = Token.objects.get_or_create(user=user)
        message = {
            'token': str(token),
            'email': email
        }
        return Response(message)


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

    # TODO :  you can uncommet this for authentication ,for now i am not using for developing 
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

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

    def destroy(self,request,pk=None):
        #DELETE /api/vendors/{vendor_id}/: Delete a vendor.
        vender_info = get_object_or_404(self.queryset, pk=int(pk))
        if vender_info:
            vender_info.delete()
        return Response('Vender is delete successfully........')
    
    @action(detail=True, methods=['get'])
    def performance(self,request,pk=None):
        vender_info = get_object_or_404(self.queryset, pk=pk)
        serializer = self.get_serializer(vender_info)
        return Response(serializer.data)
        

    

# 2. Purchase Order Tracking:

class PurchaseOrderViwset(GenericViewSet):
    '''
    ● Model Design: Track purchase orders with fields like PO number, vendor reference,
    order date, items, quantity, and status.
    ● API Endpoints:
    ● POST /api/purchase_orders/: Create a purchase order.
    ● GET /api/purchase_orders/: List all purchase orders with an option to filter by
    vendor.
    ● GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
    ● PUT /api/purchase_orders/{po_id}/: Update a purchase order.
    ● DELETE /api/purchase_orders/{po_id}/: Delete a purchase order.
    
    '''
    serializer_class = PurchaseOrderSerializer
    queryset = PurchaseOrder.objects.all()

    # TODO :  you can uncommet this for authentication ,for now i am not using for developing 
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def create(self,request):
        # POST /api/purchase_orders/: Create a purchase order.
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def list(self,request):
        # GET /api/purchase_orders/: List all purchase orders with an option to filter by vendor.
        serialized_data = self.get_serializer(self.queryset,many=True)
        return Response(serialized_data.data)
    
    def retrieve(self,request,pk=None):
        # GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
        vender_info = get_object_or_404(self.queryset, pk=pk)
        serializer = self.get_serializer(vender_info)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        # PUT /api/purchase_orders/{po_id}/: Update a purchase order.
        instance = get_object_or_404(self.queryset,pk=int(pk))
        if instance:
            serilizer = self.get_serializer(instance,data=request.data,partial=True)
            serilizer.is_valid(raise_exception=True)
            serilizer.save()
            return Response(serilizer.data)
    
    def destroy(self,request,pk=None):
        #  DELETE /api/purchase_orders/{po_id}/: Delete a purchase order.
        order = get_object_or_404(self.queryset, pk=int(pk))
        if order:
            order.delete()
        return Response('Vender is delete successfully........')
    
    @action(detail=True,methods=['GET'])
    def acknowledge(self,request,pk=None):
        order = get_object_or_404(self.queryset, pk=int(pk))
        if order:
            order.acknowledgment_date = datetime.now()
            order.save()
        return Response(f'Acknoledge is update for vender {pk}')
        
    


