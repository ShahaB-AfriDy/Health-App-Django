from django.urls import path
from Heart import views

urlpatterns = [
    path('heart/',views.Heart,name='Heart'),
    path('heart-result/',views.Heart_Result,name='Result'),
]
