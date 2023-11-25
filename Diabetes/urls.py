from django.urls import path
from Diabetes import views

urlpatterns = [
    path('diabetes/',views.Diabetes,name='Diabetes'),
    path('diabetes-result/',views.Diabetes_Result,name='Diabetes_result'),
]
