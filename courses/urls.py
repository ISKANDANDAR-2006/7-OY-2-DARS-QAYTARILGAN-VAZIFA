from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('', views.course_list, name='course_list'),
    path('courses/add/', views.add_course, name='add_course'),
    path('courses/update/<int:id>/', views.update_course, name='update_course'),
    path('courses/delete/<int:id>/', views.delete_course, name='delete_course'),
    path('courses/<int:id>/', views.course_detail, name='course_detail'),  # course_detail URL'si qo'shildi
]
