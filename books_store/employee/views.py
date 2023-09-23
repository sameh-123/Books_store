from django.shortcuts import render
from django.shortcuts import redirect, render
from .models import *
from .form import *

# Create your views here.
def admin_page(req):
    context={}
    context["user"]=req.session["username"]
    return render(req,"empolyee/admin_page.html",context)

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
                return redirect("empolyee/admin_page")
        except:
            context['warn']="there is no user with this username"
    return render(req,"employee/login_admin.html",context)

def changeadminpass(req):
    context={}
    if req.method=='POST':
        newpass=req.POST.get('password')
        if newpass== req.POST.get('confirm') :
            adminall.objects.create(username=req.POST.get('username'),password=req.POST.get('password'))
            return redirect("empolyee/admin_page")
        else :context['warn']="you didn't confirm the right password"
    return render(req, "employee/changeadminpass.html",context)

def addbook(request):
    form=bookform()
    context={'form':form}
    if request.method=='POST':
        form=bookform(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "employee/addbook.html",context)

def allbooks(req):
    context={}
    context["user"]=req.session["username"]
    books=book.objects.all()
    context["books"]=books
    return render(req,"empolyee/allbooks.html",context)


def allusers(req):
    context={}
    context["user"]=req.session["username"]
    stds=student.objects.all()
    context["users"]=stds
    return render(req,"empolyee/allusers.html",context)

def deletebook(req,id):
    book.objects.filter(id=id).delete()
    return redirect("empolyee/all_books")



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