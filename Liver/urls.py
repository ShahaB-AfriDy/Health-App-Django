from django.urls import path
from Liver import views

urlpatterns = [
    path('liver/',views.Liver,name='Liver'),
    path('liver-result/',views.Liver_Result,name='liver_result'),
]
