from django.shortcuts import render,HttpResponseRedirect
from Kidney.form import Kedney_Form
from joblib import load
from numpy import array
Model_path = "E:\Python in Sublime\DJango Framework\Health App Django\Health_APP\Kidney\static\model\kidney_model.pkl"

predicted_value = None
# Create your views here.
def Kidney_fun(request):
    if request.method == 'POST':
        global predicted_value
        kidney_form = Kedney_Form(request.POST)
        if kidney_form.is_valid():

            input_list = kidney_form.cleaned_data.values()
            input_list = list(map(float,input_list))
            input_list = array(input_list).reshape(1,7)
            predicted_value = load_model(input_list)
            # print(f"prediction value: {predicted_value}")
            kidney_form = Kedney_Form()
            return HttpResponseRedirect("/kidney-result/")
        
    else:
        kidney_form = Kedney_Form()
    return render(request,template_name='kidney.html',context={"kidney_form":kidney_form})



def Kidney_Result(request):
    if predicted_value:
        result = "Sorry your chances of getting the disease. Please consult the doctor immediately."
    else:
        result = "No need to fear. You have no dangerous symptoms of the disease"
    return render(request,template_name='kidney_result.html',context={"prediction":result})


def load_model(Input_data):
    model = load(Model_path)
    result = model.predict(Input_data)
    return result[0]