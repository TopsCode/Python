from django.shortcuts import render
from .forms import MyForm
from django.template import loader
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request,"example_app/myfile.html")    

def responseform(request):

     if request.method == 'POST':
        
        myForm = MyForm(request.POST)

        if myForm.is_valid():
            name = myForm.cleaned_data['name']
            email = myForm.cleaned_data['email']
            contact=myForm.cleaned_data['contact']
            feedback = myForm.cleaned_data['feedback']

            context = {
            'name': name,
            'email': email,
            'contact':contact,
            'feedback': feedback
            }

            template = loader.get_template('example_app/thankyou.html')

            return HttpResponse(template.render(context, request))



     else:
         form = MyForm()

     return render(request, 'example_app/response.html', {'form':form})
