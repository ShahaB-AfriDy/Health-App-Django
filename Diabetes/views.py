from django.shortcuts import render,HttpResponseRedirect
from Diabetes.form import Diabetes_Form
from joblib import load
from numpy import array

Model_path = "E:\Python in Sublime\DJango Framework\Carouselslider\Slider\Diabetes\model\diabetes_model.pkl"



# # Create your views here.
# def Diabetes(request):
#     return render(request,template_name='diabetes.html')

predicted_value = None

# Create your views here.
def Diabetes(request):
    if request.method == 'POST':
        global predicted_value
        diabetes_form = Diabetes_Form(request.POST)
        if diabetes_form.is_valid():

            input_list = diabetes_form.cleaned_data.values()
            input_list = list(map(float,input_list))
            input_list = array(input_list).reshape(1,6)
            predicted_value = load_model(input_list)
            # print(f"prediction value: {predicted_value}")

            diabetes_form = Diabetes_Form()
            return HttpResponseRedirect("/diabetes-result/")
        
    else:
        diabetes_form = Diabetes_Form()
    return render(request,template_name='diabetes.html',context={"diabetes_form":diabetes_form})







def Diabetes_Result(request):
    if predicted_value:
        result = "Sorry your chances of getting the disease. Please consult the doctor immediately"
    else:
        result = "No need to fear. You have no dangerous symptoms of the disease"
    return render(request,template_name='diabetes_result.html',context={"prediction":result})


def load_model(Input_data):
    model = load(Model_path)
    result = model.predict(Input_data)
    return result[0]