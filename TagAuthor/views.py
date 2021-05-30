from django.shortcuts import get_object_or_404, redirect, render

from django.http import HttpResponse
from .models import AuthorModel
from Tags.models import TagRequest


# Create your views here.

def home(request):
    if request.session.has_key('authorid'):
        id =  request.session['authorid']
        author=AuthorModel.objects.get(id=id)
        requests = TagRequest.objects.all()
        # return HttpResponse(author)
        return render(request,"home.html",{'author':author,'request':requests})

    else:
        return redirect("/author/login")


def login(request):
    if request.session.has_key('authorid'):
        return redirect("/author/home")
    else:
        if request.method=="POST":
            userLoged=AuthorModel.objects.filter(a_username=request.POST.get("username"),a_pass=request.POST.get("password")).count()
            if userLoged>0:
                user=get_object_or_404(AuthorModel, a_username=request.POST.get("username"),a_pass=request.POST.get("password"))
                request.session["authorid"]=user.id
                return redirect("/author/home")
            else:
                return render(request,"login.html",{'fail':1})
        return render(request,"login.html",{})


def logout(request):
    request.session.flush()
    return redirect("/author/login")
