from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserLoginSerializer
from .models import User
from rest_framework.views import APIView
from django.contrib.auth import authenticate

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            print(user)
            if user:
                return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():  
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            # Perform authentication (e.g., check credentials)
            # Assuming you have a CustomUser model
            user = User.objects.filter(email=email).first()
            if user and user.password == password:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'access': str(refresh.access_token),
                    'refresh': str(refresh),
                    'type': str(user.type)
                })
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AdminLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():  
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            # Perform authentication (e.g., check credentials)
            # Assuming you have a CustomUser model
            print(email,password)
            user = User.objects.filter(email=email).first()
            myuser = authenticate(username=user.username,password=password)
            print(myuser)
            if myuser and user.is_superuser:
                print(user)
                refresh = RefreshToken.for_user(user)
                return Response({
                    'access': str(refresh.access_token),
                    'refresh': str(refresh),
                    'type': 'is_admin'
                })
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListAPIView(APIView):
  def get(self, request):
    users = User.objects.filter(type='author')  # Fetch all users
    serializer = UserSerializer(users, many=True)  # Serialize data (optional)
    return Response(serializer.data, status=status.HTTP_200_OK)