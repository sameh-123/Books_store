from django.shortcuts import render
from django.shortcuts import redirect, render
from .models import *
# Create your views here.
def admin_page(req):
    return render(req,"employee/admin-page.html")

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
        return render(req,"loginadmin",context)

def changeadminpass(req):
    context={}
    if req.method=='POST':
        if req.POST.get('password')== req.POST.get('confirm') and req.POST.get('username')!='' :
            obj=adminall()
            adminall.objects.create(username=req.POST.get('username'),password=req.POST.get('password'))
            stud=adminall.objects.get(username=req.POST.get('username'))
            req.session["id"] = stud.id
            req.session["username"] = stud.username
            return redirect("/admin-page")
        else :context['warn']="you didn't confirm the right password"
    return render(req, "employee/changeadminpass.html",context)