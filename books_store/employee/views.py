from django.shortcuts import render
from django.shortcuts import redirect, render
from .models import *
from home.models import *
# Create your views here.
def admin_page(req):
    context={}
    context["user"]=req.session["username"]
    return render(req,"admin-page.html",context)

def loginadmin(req):
    context={}
    if req.method=='POST':
        admin_name=req.POST.get('username')
        try:
            stud=adminall.objects.get(username=admin_name)
            student_pass=req.POST.get('password')
            if stud.password != student_pass:
                context['warn2']="incorrect password"
            else:
                req.session["id"] = stud.id
                req.session["username"] = stud.username
                return redirect("/admin-page")
        except:
            context['warn']="there is no user with this username"
    return render(req,"login_admin.html",context)

def changeadminpass(req):
    context={}
    if req.method=='POST':
        newpass=req.POST.get('password')
        if newpass== req.POST.get('confirm') :
            adminall.objects.create(username=req.POST.get('username'),password=req.POST.get('password'))
            return redirect("/admin-page")
        else :
            context['warn']="you didn't confirm the right password"
    return render(req, "changepass.html",context)

def logout(req):
    del req.session["id"]
    del req.session["username"]
    return redirect("/loginadmin")

def allbooks(req):
    context={}
    context["user"]=req.session["username"]
    books=book.objects.all()
    context["books"]=books
    return render(req,"allbooks.html",context)


def allusers(req):
    context={}
    context["user"]=req.session["username"]
    stds=student.objects.all()
    context["users"]=stds
    return render(req,"allusers.html",context)

def deletebook(req,id):
    book.objects.filter(id=id).delete()
    return redirect("/all_books")

def addbook(req):
    context={}
    if req.method=='POST':
        obj=book()
        book.objects.create(name=req.POST.get('name'))
        return redirect("/all_books")
    return render(req,"addbook.html",context)

def search(req):
    context={}
    if req.method=='POST':
        name=req.POST.get('id')
        students=student.objects.filter(student_id=str(id))
        if len(students)!=1 :
            context['warn']="there is no user with this id"
            return render(req,"search.html",context)
        students=students[0]
        context["user"]=students
        context["books"]=Borrow.objects.filter(student_id=str(id))
        return render(req,"search.html",context)
    return render(req,"search.html",context)