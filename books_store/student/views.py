from django.shortcuts import render
from .form import *
# Create your views here.


def add_book(request):
    context={}
    form=bookform()
    context={'form':form}
    if request.method=='POST':
        form=bookform(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "student/add_book.html",context)
