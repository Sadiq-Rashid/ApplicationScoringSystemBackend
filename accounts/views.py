from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from accounts.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login as auth, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login as django_login
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.models import Roles


# Create your views here.
@csrf_exempt
@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'response': 'user account created succesifully'}, status=status.HTTP_201_CREATED)
    return Response({"error": "user account failed to be created"}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        django_login(request, user)

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        userId = request.user.id
        print("userId", userId)

        try:
            user_role = Roles.objects.get(user=request.user).roleName  
           
        except Roles.DoesNotExist:
            user_role = 'user'

        return Response({'message': 'Login successful', 'access_token': access_token,  'role': user_role , 'username': username, "userId": userId}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    

    
   

# @api_view(['POST'])
# def login(request):
#     username = request.data.get("username")
#     password = request.data.get("password")

#     user = authenticate(request, username=username, password=password)

#     if user is not None:
#         login(request, user)
#         return Response({'response': 'user login succesifull'}, status=status.HTTP_200_OK)
#     return Response({'response': 'an error occured while trying to login'}, status=status.HTTP_400_BAD_REQUEST)



