# forms.py
from django import forms

class Kedney_Form(forms.Form):
    
    Blood_Pressure = forms.IntegerField(min_value=50,max_value=180,widget=forms.TextInput(attrs={'class': 'form-control',"placeholder":"Blood Pressure"}))
    Specific_Gravity = forms.FloatField(min_value=1.005,max_value=1.025,widget=forms.TextInput(attrs={'class': 'form-control',"placeholder":"Specific Gravity"}))
    Albumin = forms.FloatField(min_value=0.0,max_value=5.0,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Albumin'}))
    Blood_Sugar_Level = forms.FloatField(min_value=0.0,max_value=5.0,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Blood Sugar Level'}))
    Red_Blood_Cells_Count = forms.FloatField(min_value=0,max_value=1,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"Red Blood Cells Count"}))
    Pus_Cell_Count = forms.FloatField(min_value=0,max_value=1,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Pus Cell Count'}))
    Pus_Cell_Clumps = forms.FloatField(min_value=0,max_value=1,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Pus Cell Clumps'}))



