from django.urls import path
from Kidney import views

urlpatterns = [
    path('kidney/',views.Kidney_fun,name='Kidney'),
    path('kidney-result/',views.Kidney_Result,name='kidney_result'),
]
