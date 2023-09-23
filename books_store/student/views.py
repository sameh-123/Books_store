from django.shortcuts import render
# Create your views here.
from home.models import *

def borrow_book(request):
    context={}
    context['user']=request.session['username']
    if request.method=='POST':
        id=request.session['id']
        book_name=request.POST.get('name')
        date=request.POST.get('date')
        book_id=book.objects.get(name=book_name)
        Borrow.objects.create(student_id=str(id),book_id=str(book_id.id),date_end=date)

    return render(request, "student/borrow_book.html",context)

def update(request):
    context={}
    user=request.session['username']
    context['user']=user
    curs=student.objects.get(username=user)
    cur=curs.password
    if request.method=='POST':
        cur_pass=request.POST.get('cpassword')
        passw=request.POST.get('password')
        con=request.POST.get('confirm')
        if cur!=cur_pass:
            context['warn1']="your current password is incorrect"
        elif passw!=con:
            context['warn']="you didn't confirm the right password"
        else:
            id=request.session['id']
            std=student.objects.get(id=str(id))
            std.password=passw
            std.save()
    return render(request,"student/update.html",context)
