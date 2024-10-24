from django.urls import path
from . import views

app_name = 'report' #application name

urlpatterns = [
    path('report/', views.report_list, name='report_list'),
    path('report/<int:pk>/', views.report_detail, name='report_detail'),
]
