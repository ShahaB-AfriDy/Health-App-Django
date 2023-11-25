# forms.py
from django import forms

class Liver_Form(forms.Form):

    Total_Bilirubin = forms.FloatField(min_value=0.4,max_value=75.0,widget=forms.TextInput(attrs={'class': 'form-control',"placeholder":"Enter the Total Bilirubin"}))
    Direct_Bilirubin = forms.FloatField(min_value=0.1,max_value=19.7,widget=forms.TextInput(attrs={'class': 'form-control',"placeholder":"Enter the Direct Bilirubin"}))
    Alkaline_Phosphotase = forms.IntegerField(min_value=63,max_value=2110,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter the Alkaline Phosphotase'}))
    Alamine_Aminotransferase = forms.IntegerField(min_value=10,max_value=2000,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter the Alamine Aminotransferase'}))
    Total_Protiens = forms.FloatField(min_value=2.7,max_value=9.6,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"Enter the Total Protiens"}))
    Albumin = forms.FloatField(min_value=0.9,max_value=5.5,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter the Albumin'}))
    Albumin_and_Globulin_Ratio = forms.FloatField(min_value=0.2,max_value=2.9,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"Enter the Albumin and Globulin Ratio"}))
    



