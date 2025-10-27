from django.shortcuts import get_object_or_404, redirect, render

from django.http import HttpResponse
from .models import AuthorModel
from Tags.models import TagRequest,Tagmodel



# Create your views here.

def home(request):
    if request.session.has_key('authorid'):
        id =  request.session['authorid']
        author=AuthorModel.objects.get(id=id)
        requests = TagRequest.objects.all().order_by('tr_date').reverse()
        # return HttpResponse(author)
        return render(request,"home.html",{'author':author,'request':requests})

    else:
        return redirect("/tagauthor/login")


def login(request):
    if request.session.has_key('authorid'):
        return redirect("/tagauthor")
    else:
        if request.method=="POST":
            userLoged=AuthorModel.objects.filter(a_username=request.POST.get("username"),a_pass=request.POST.get("password")).count()
            if userLoged>0:
                user=get_object_or_404(AuthorModel, a_username=request.POST.get("username"),a_pass=request.POST.get("password"))
                request.session["authorid"]=user.id
                return redirect("/tagauthor")
            else:
                return render(request,"login.html",{'fail':1})
        return render(request,"login.html",{})


def logout(request):
    request.session.flush()
    return redirect("/tagauthor/login")


def delete(request,id):
    TagRequest.objects.get(id=id).delete()
    id =  request.session['authorid']
    author=AuthorModel.objects.get(id=id)
    requests = TagRequest.objects.all()
    return render(request,"home.html",{'author':author,'request':requests , 'flag':1})


def insert(request):
    
    if request.session.has_key('authorid'):

        id =  request.session['authorid']
        author=AuthorModel.objects.get(id=id)
        requests = TagRequest.objects.all()

        if request.method=="POST" and request.FILES:
            t=Tagmodel()
            t.tag_title=request.POST.get("tagtitle")
            t.tag_name=request.POST.get("tagname")
            t.tag_image=request.FILES.get("tagimage")
            t.tag_disc=request.POST.get("tagdesc")
            t.t_country=request.POST.get("tagcountry")
            t.t_state=request.POST.get("tagstate")
            t.t_place=request.POST.get("tagplace")
       
            
            t.save()
            t.tag_image=request.FILES.get("tagimage")
           
            
            return render(request,"home.html",{'author':author,'request':requests , 'add':1})


    else:
        return redirect("/tagauthor/login")