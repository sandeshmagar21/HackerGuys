from django.http import HttpResponse
from django.shortcuts import render
 
def view_helloworld(request):
    return HttpResponse("Hello World")
 
def view_indexpage(request):
    return render(request,'index.htm')
