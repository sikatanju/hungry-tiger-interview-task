from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import RegisterUserSerializer

class RegisterView(APIView):
    http_method_names = ['post']
    
    def post(self, request, *args, **kwargs):
        user_type = kwargs.get('user_type')
        serializer = RegisterUserSerializer(data=request.data, context={'user_type': user_type})
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)