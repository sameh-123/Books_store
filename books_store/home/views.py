from django.shortcuts import *
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.shortcuts import redirect, render
@csrf_exempt
# Create your views here.
def home(request):
    return render(request, "home/homebase.html")
def student_page(request):
    user_id=request.session["id"]
    books=Borrow.objects.filter(student_id=str(user_id))
    context={}
    context['books']=books
    context['user']=request.session["username"]
    return render(request,"home/student_page.html",context)
def signin(request):
    context={}
    if request.method=='POST':
        student_name=request.POST.get('username')
        try:
            stud=student.objects.get(username=student_name)
            student_pass=request.POST.get('password')
            if stud.password != student_pass:
                context['warn2']="incorrect password"
                return render(request, "home/signin.html",context)
            else:
                books=Borrow.objects.filter(student_id=str(stud.id))
                context['books']=books
                request.session["id"] = stud.id
                request.session["username"] = stud.username
                return redirect("/student_page")
        except:
            context['warn']="there is no user with this username"
    else : return render(request, "home/signin.html",context)
def signup(request):
    context={}
    if request.method=='POST':
        if request.POST.get('password')== request.POST.get('confirm') and request.POST.get('username')!='' :
            obj=student()
            student.objects.create(username=request.POST.get('username'),password=request.POST.get('password'))
            stud=student.objects.get(username=request.POST.get('username'))
            request.session["id"] = stud.id
            request.session["username"] = stud.username
            return redirect("/student_page")
        else :context['warn']="you didn't confirm the right password"
    return render(request, "home/signup.html",context)