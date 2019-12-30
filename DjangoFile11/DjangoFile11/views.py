from django.http import HttpResponse
from django.shortcuts import render

def view_hello(request):
    return HttpResponse("<h1>Hello World</h1>")

def view_hello_world_page(request):
    return render(request,'index.html')

def view_Form(request):
    return render(request,'Form.html')

def view_Form_data(request):
    Form_data =request.GET['username']
    return render(request,'index.html',{'usernamekey':Form_data})