from django.shortcuts import render
from django.shortcuts import redirect, render
from .models import *
from .form import *

# Create your views here.
def admin_page(req):
    context={}
    if 'id' not in req.session:
        return redirect("/loginadmin")
    context["user"]=req.session["username"]
    return render(req,"admin_page.html",context)

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
                return redirect("/admin_page")
        except:
            context['warn']="there is no user with this username"
    return render(req,"login_admin.html",context)

def changeadminpass(request):
    context={}
    if 'id' not in request.session:
        return redirect("/loginadmin")
    user=request.session['username']
    context['user']=user
    curs=adminall.objects.get(username=user)
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
            std=adminall.objects.get(id=str(id))
            std.password=passw
            std.save()
            return redirect("/admin_page")
    return render(request, "changepass.html",context)

def addbook(request):
    if 'id' not in request.session:
        return redirect("/loginadmin")
    form=bookform()
    context={'form':form}
    if request.method=='POST':
        form=bookform(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "addbook.html",context)

def allbooks(req):
    context={}
    if 'id' not in req.session:
        return redirect("/loginadmin")
    context["user"]=req.session["username"]
    books=book.objects.all()
    context["books"]=books
    return render(req,"allbooks.html",context)


def allusers(req):
    context={}
    if 'id' not in req.session:
        return redirect("/loginadmin")
    context["user"]=req.session["username"]
    stds=student.objects.all()
    context["users"]=stds
    return render(req,"allusers.html",context)

def deletebook(req,id):
    if 'id' not in req.session:
        return redirect("/loginadmin")
    book.objects.filter(id=id).delete()
    return redirect("/all_books")



def search(request):
    if 'id' not in request.session:
        return redirect("/loginadmin")
    user_id=request.POST.get('id')
    books=Borrow.objects.filter(student_id=str(user_id))
    std=student.objects.get(id=str(user_id))
    context={}
    context['books']=books
    context['user']=std.username
    request.session['idd']=std.id
    return render(request,"search.html",context)


def rett(request,id):
    context={}
    if 'id' not in request.session:
        return redirect("/loginadmin")
    user_id=request.session['idd']
    Borrow.objects.filter(book_id=str(id),student_id=str(user_id)).delete()
    books=Borrow.objects.filter(student_id=str(user_id))
    context['books']=books
    context['user']=student.objects.get(id=str(user_id)).username
    request.session["id"] = user_id
    request.session["username"] = student.objects.get(id=str(user_id)).username
    return render(request,'search.html',context)

def logout(req):
    del req.session['id']
    del req.session['username']
    return redirect("/loginadmin")