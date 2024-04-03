from django.urls import path
from application import views

urlpatterns = [
    path('create_application/', views.createApplication, name='create_application'),
    path('get_application/', views.getApplication, name='get_application'),
    path('applications/', views.viewApplications, name='applications'),
    path('applications/<int:pk>/', views.viewApplication, name='application'),
    path('update_application/<int:pk>/', views.updateApplication, name='update_application'),
    path('delete_application/<int:pk>/', views.deleteApplication, name='delete_application'),



    path('user_application/', views.viewApplicationsAsUser, name='user_application'),
    path('users/', views.getUserDetails, name='users')
]