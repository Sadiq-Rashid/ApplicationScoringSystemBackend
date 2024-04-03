from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from application.models import Application
from application.serializers import ApplicationSerializer
from accounts.models import Roles
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from accounts.serializers import UserDataSerializer
# Create your views here.


@api_view(['GET'])
def getUserDetails(request):
    users = User.objects.all()
    serializer = UserDataSerializer(users, many=True)  
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def viewApplications(request):
    user = request.user

    try:
        role = Roles.objects.get(user=user).roleName
    except Roles.DoesNotExist:
        role = 'user'

    if role == 'admin':
        applications = Application.objects.all()
    else:
        applications = Application.objects.filter(user=user)

    count = applications.count()
    serializers = ApplicationSerializer(applications, many=True)

    data = {
        'count': count,
        'data': serializers.data
    }
    return Response(data, status=status.HTTP_200_OK)






@api_view(['GET'])
def viewApplicationsAsUser(request):
    application = Application.objects.get(user=request.user)
    serializers = ApplicationSerializer(application)
    return Response(serializers.data, status=status.HTTP_200_OK)



@api_view(['GET'])
def viewApplication(request, pk):
    try:
        application = Application.objects.get(pk=pk)
    except Application.DoesNotExist:
        return Response({'error': 'application with that id not found'}, status=status.HTTP_204_NO_CONTENT)  

    serializer = ApplicationSerializer(application)
    return Response(serializer.data, status=status.HTTP_200_OK) 


@api_view(['GET'])
def getApplication(request, pk):
    try:
        application = Application.objects.get(pk=pk)
    except Application.DoesNotExist:
        return Response({'error': 'application with that id not found'}, status=status.HTTP_204_NO_CONTENT)  

    serializer = ApplicationSerializer(application)
    return Response(serializer.data, status=status.HTTP_200_OK) 


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def createApplication(request):
    
    serializer = ApplicationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateApplication(request, pk):
    try:
        application = Application.objects.get(pk=pk)
    except Application.DoesNotExist:
        return Response({'error': 'application with that id not found'}, status=status.HTTP_204_NO_CONTENT)  
    

    serializer = ApplicationSerializer(application, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['DELETE'])
def deleteApplication(request, pk):
    try:
        application = Application.objects.get(pk=pk)
    except Application.DoesNotExist:
        return Response({'error': 'Application with that id not found'}, status=status.HTTP_204_NO_CONTENT)    
    
    application.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
    