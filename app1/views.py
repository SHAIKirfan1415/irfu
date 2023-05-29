from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def apps1(request):
    return HttpResponse('this my project6')

def appweb1(request):
    return render(request,'appweb1.html')
