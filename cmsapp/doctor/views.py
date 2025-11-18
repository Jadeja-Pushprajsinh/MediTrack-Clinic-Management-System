from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from doctor.models import *

def show_login(request):
    return render(request , 'login_form.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')

        if email == 'admin@gmail.com' and pwd == 'admin@123':
            return redirect('show_dashboard')

        else:
            return HttpResponse("<script>alert('Incorrect username or password'); window.location.href='/';</script>")
    
    return HttpResponse(show_login)

def show_register(request):
    return render(request , 'register_form.html')


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        fname = request.POST.get('first_name') 
        lname = request.POST.get('last_name')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        created_at = request.POST.get('created_at')
        allergies = request.POST.get('allergies')
        address = request.POST.get('address')

        user = Register(email = email , pwd = pwd , fname = fname , lname = lname , phone = phone , dob = dob , created_at = created_at, allergies = allergies , address = address)
        user.save()
        return HttpResponse("<script> alert('SUCCESS'); window.location.href=''; </script>")
        
def register_patient(request):
        return HttpResponse("<script> alert('SUCCESS'); window.location.href=''; </script>")
