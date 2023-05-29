from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def apps2(request):
    return HttpResponse('this my project6')

def appweb2(request):
    return render(request,'appweb2.html')

