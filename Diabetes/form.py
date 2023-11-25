# forms.py
from django import forms

class Diabetes_Form(forms.Form):
    
    Number_of_Pregnencies = forms.IntegerField(min_value=0,max_value=15,widget=forms.TextInput(attrs={'class': 'form-control',"placeholder":"No. of Pregnencies"}))
    Glucose_Level = forms.IntegerField(min_value=0,max_value=199,widget=forms.TextInput(attrs={'class': 'form-control',"placeholder":"Glucose Level"}))
    Current_Blood_Pressure = forms.IntegerField(min_value=0,max_value=122,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Current Blood Pressure'}))
    Enter_the_Body_Mass_Index = forms.FloatField(min_value=0.0,max_value=67.1,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Body Mass Index'}))
    Diabetes_Pedigree_Function = forms.FloatField(min_value=0.078,max_value=2.42,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"Diabetes Pedigree Function"}))
    Age = forms.IntegerField(min_value=20,max_value=82,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Age'}))
    



