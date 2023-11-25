from django.shortcuts import render,HttpResponseRedirect,redirect
from Heart.form import Heart_Form
from  pickle import load
from numpy import array
import joblib
# Create your views here.
Model_path = "E:\Python in Sublime\DJango Framework\Carouselslider\Slider\Heart\static\model\heart_model.pkl"

predicted_value = None

# def Heart(request):
#     return render(request,template_name='heart.html')

def Heart(request):
    if request.method == 'POST':
        global predicted_value
        heart_form = Heart_Form(request.POST)
        if heart_form.is_valid():
            input_list = heart_form.cleaned_data.values()
            input_list = list(map(float,input_list))
            # print(input_list)
            predicted_value = load_model(array(input_list).reshape(1,7))
            heart_form = Heart_Form()
            return HttpResponseRedirect("/heart-result/")
    else:
        heart_form = Heart_Form()
    return render(request,template_name='heart.html',context={"heart_form":heart_form})



def Heart_Result(request):
    if predicted_value:
        result = "Sorry, your chances of getting the disease are high. Please consult the doctor immediately."
    else:
        result = "No need to fear. You have no dangerous symptoms of the disease"
        
    return render(request,template_name='heart_result.html',context={"prediction":result})


def load_model(Input_data):
    model = joblib.load(Model_path)
    result = model.predict(Input_data)
    return result[0]