from django.shortcuts import render
from .models import *
from django.utils.datastructures import MultiValueDictKeyError

def index(request):
    if request.method == "POST" :
        a = port()
        a.name=request.POST['name']
        a.mail=request.POST['mail']
        a.subject=request.POST['subject']
        a.mesage = request.POST['mesage']
    
    return render(request, 'index.html')
