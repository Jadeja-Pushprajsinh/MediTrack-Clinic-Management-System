from django.shortcuts import render

def show_dashboard(request):
    return render(request,'dashboard.html')

def show_add_patient(request):
    return render(request , 'register_form.html')

