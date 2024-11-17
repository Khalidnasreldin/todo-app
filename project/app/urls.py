from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index_view, name=''),
    path('update-task/<str:pk>/', views.update_task_view, name='update-task'),
    path('delete-task/<str:pk>/', views.delete_task_view, name='delete-task'),
]
