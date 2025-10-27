
from django.shortcuts import render,redirect
from django.http import HttpResponse
from User.models import UserModel
from django.db.models import Count
from TagAuthor.models import AuthorModel
# Create your views here.


def admiHome(request):
    if request.session.has_key('adminId'):
        return render (request,"admin.html")

    else:
        return redirect("/admin/login")


def ProofDetail(request,username):
    if request.session.has_key('adminId'):
        user = UserModel.objects.get(u_name__iexact =  username)
        return render (request,"proof.html",{'user':user})

    else:
        return redirect("/admin/login")


def userVerify(request,id):
    
    user  = UserModel.objects.get(id=id)
    
    if request.method == 'POST':
        radio = request.POST.get("anontype")
        
        if radio == '0':
            
            user.u_verified ='1'
            user.save()
            return redirect('/admin')
            
        elif radio =='1':
            
            user.u_verified = '0'
            user.save()
            return redirect('/admin')


def insert(request):
    if request.session.has_key('adminId'):
        if request.method == 'POST':
            a = AuthorModel()

            a.a_name = request.POST.get("authorname")
            a.a_age = request.POST.get("authorage")
            a.a_loctype = request.POST.get("loctype")
            a.a_location = request.POST.get("authorcountry")
            a.a_username = request.POST.get("authorusername")
            a.a_pass = request.POST.get("authorpass")
            a.save()

            return render (request,"admin.html",{'flag':1})
    else:
        return redirect("/admin/login")






def adminLogin(request):
    if request.session.has_key('adminId'):
        return redirect("/admin")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            username = str(username)
            password = str(password)

            if username == "xadmin" and password == "x1234":
                request.session["adminId"] = username

                return redirect("/admin")
            else:
                return render (request,"admin-login.html",{'flag':1})
        return render(request,"admin-login.html",{})


def logout(request):
    request.session.flush()
    return redirect("/admin/login")



    
