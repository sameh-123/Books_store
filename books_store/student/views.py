from django.shortcuts import render
from home.models import *
# Create your views here.
def allbooks(req):
    books=book.objects.filter(name=None)
    context={books}
    return render(req, 'allbooks.html',context)

def logout(req):
    req.session['userid']=None
    return render(req, 'index.html')
