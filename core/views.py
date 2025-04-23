from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import RegisterCustomerSerializer
from hungry_app.models import Customer, Vendor

class RegisterView(APIView):
    http_method_names = ['post']
    
    def post(self, request, *args, **kwargs):
        user_type = kwargs.get('user_type')
        serializer = RegisterCustomerSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user_type == 'customer':
                user.is_customer=True
                Customer.objects.create(user=user)
            elif user_type == 'vendor':
                user.is_vendor=True
                Vendor.objects.create(user=user)

            user.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)