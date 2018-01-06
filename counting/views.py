from django.shortcuts import render

# Create your views here.
def countdown(request):
    return render(request,'counting/countdown.html')
