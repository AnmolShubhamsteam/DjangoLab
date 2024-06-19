from django.shortcuts import render,redirect
from core.forms import *
from django.views.generic import ListView,DetailView
# Create your views here.
def home(request):
    return render(request,"home.html",{})

def form_user(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = StudentForm()
    
    return render(request, 'form.html', {'form': form})

class Lst(ListView):
    model=Student
    template_name="List.html"
