from django.shortcuts import render,HttpResponseRedirect
from Liver.form import Liver_Form
from joblib import load
from numpy import array

# Create your views here.
# def Liver(request):
#     return render(request,template_name='liver.html')


Model_path = "E:\Python in Sublime\DJango Framework\Health App Django\Health_APP\Liver\static\model\liver_model.pkl"



# # Create your views here.
# def Diabetes(request):
#     return render(request,template_name='diabetes.html')

predicted_value = None
# Create your views here.
def Liver(request):
    if request.method == 'POST':
        global predicted_value
        liver_form = Liver_Form(request.POST)
        if liver_form.is_valid():

            input_list = liver_form.cleaned_data.values()
            input_list = list(map(float,input_list))
            input_list = array(input_list).reshape(1,7)
            predicted_value = load_model(input_list)
            # print(f"prediction value: {predicted_value}")

            liver_form = Liver_Form()
            return HttpResponseRedirect("/liver-result/")
        
    else:
        liver_form = Liver_Form()
    return render(request,template_name='liver.html',context={"liver_form":liver_form})






def Liver_Result(request):
    if predicted_value:
        result = "Sorry your chances of getting the disease. Please consult the doctor immediately."
    else:
        result = "No need to fear. You have no dangerous symptoms of the disease"
    return render(request,template_name='liver_result.html',context={"prediction":result})


def load_model(Input_data):
    model = load(Model_path)
    result = model.predict(Input_data)
    return result[0]