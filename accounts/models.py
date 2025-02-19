from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Roles(models.Model):

    ROLES = (
        ('user', 'user'),
        ('admin', 'admin')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    id = models.AutoField(primary_key=True)
    roleName = models.CharField(max_length=100, choices=ROLES)


    def __str__(self):
        return f"{self.roleName} - {self.user.username}"