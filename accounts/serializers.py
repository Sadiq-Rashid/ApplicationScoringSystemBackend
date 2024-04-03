from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import Roles




class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['username', 'first_name', 'last_name', 'last_name', 'email', 'date_joined']
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={
                                     'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={
                                      'input_type': 'password'})
    role = serializers.CharField(write_only=True, required=False, default='user')  # Add role field

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password", "password2", "role"]  # Include role field in fields list
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True},
        }

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("The two passwords must match.")
        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        role_name = validated_data.pop('role', 'user') 
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data, password=password)
        role, created = Roles.objects.get_or_create(roleName=role_name, user=user)
        return user

