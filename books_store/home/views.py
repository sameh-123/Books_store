from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *

@csrf_exempt
# Create your views here.
def home(request):
    return render(request, "home/homebase.html")

def signin(request,id):
    context={}
    if request.method=='POST':
        stud=student.objects.get(id=id)
        if stud==None:
            context['warn']="there is no user with these data"
        else:
            return render(request, "home/signin.html")
    return render(request, "home/signin.html")
def signup(request):
    context={}
    if request.method=='POST':
        if request.POST.get('password')== request.POST.get('confirm') :
            obj=student()
            student.objects.create(username=request.POST.get('username'),password=request.POST.get('password'))
            context['msg']="you are registered succesfuly , you can sign in now"
        else :context['warn']="you didn't confirm the right password"
    return render(request, "home/signup.html",context)