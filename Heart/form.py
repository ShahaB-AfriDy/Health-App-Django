# forms.py
from django import forms

class Heart_Form(forms.Form):
    pain_types = [
        ('1', 'Typical Angina'),
        ('2', 'Aytpical Angina'),
        ('3', 'Non-Anginal pain'),
        ('4', 'Asymptomatic'),
    ]

    chest_pain_type = forms.ChoiceField(choices=pain_types, widget=forms.Select(attrs={'class': 'form-control',"placeholder":None}))

    resting_blood_pressure = forms.IntegerField(min_value=94,max_value=200,label="Resting Blood Pressure (in mm Hg)",
                                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    serum_cholestoral = forms.IntegerField(min_value=126,max_value=564,label="Serum Cholestoral in mg/dl",
                                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    fasting_blood_sugar_choices = [
        ('0', 'Fasting Blood Sugar < 120 mg/dl'),
        ('1', 'Fasting Blood Sugar > 120 mg/dl'),
    ]

    Fasting_Blood_Sugar = forms.ChoiceField(choices=fasting_blood_sugar_choices, label="Fasting Blood Sugar",
                                            widget=forms.Select(attrs={'class': 'form-control',"placeholder":None}))
    Resting_Electro_choices = [
        ('0', 'Normal'),
        ('1', 'having St-T wave abnormality'),
        ('2', 'showing probable or definite left ventricular hypertrophy'),
    ]

    Resting_Electro_cardiographic_Result = forms.ChoiceField(choices=Resting_Electro_choices,label="Resting Electro-cardiographic Result",
                                                              widget=forms.Select(attrs={'class': 'form-control',"placeholder":None}))
    Maximum_Heart_Rate_Achieved = forms.IntegerField(min_value=71,max_value=202,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Excercise = [
        ('1', 'Yes'),
        ('0', 'No'),
    ]
    Exercise_Induced_Angina = forms.ChoiceField(choices=Excercise, label="Exercise Induced Angina",
                                                widget=forms.Select(attrs={'class': 'form-control',"placeholder":None}))



