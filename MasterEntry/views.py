
from django.shortcuts import render,redirect
from django.http import HttpResponse
from User.models import tempProof,UserModel
from django.db.models import Count
from TagAuthor.models import AuthorModel
# Create your views here.


def admiHome(request):
    if request.session.has_key('adminId'):
        proofs = tempProof.objects.all().values('name').annotate(dcount=Count('name')).order_by()
        return render (request,"admin.html",{'proofs':proofs})

    else:
        return redirect("/xadmin/login")


def ProofDetail(request,username):
    if request.session.has_key('adminId'):
        # username = str(username)
        proofs = tempProof.objects.filter(name__iexact=username)

        user = UserModel.objects.get(u_name__iexact =  username)
        return render (request,"proof.html",{'user':user,'proofs':proofs})

    else:
        return redirect("/xadmin/login")


def userVerify(request,id):
    
    user  = UserModel.objects.get(id=id)
    
    if request.method == 'POST':
        radio = request.POST.get("anontype")
        
        if radio == '0':
            
            user.u_verified ='1'
            user.save()
            return redirect('/xadmin')
            
        elif radio =='1':
            
            user.u_verified = '0'
            user.save()
            return redirect('/xadmin')


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

            proofs = tempProof.objects.all().values('name').annotate(dcount=Count('name')).order_by()
            return render (request,"admin.html",{'proofs':proofs,'flag':1})
    else:
        return redirect("/xadmin/login")


def viewProof(request,id):
    if request.session.has_key('adminId'):
        image = tempProof.objects.get(id=id)
        return render (request,"viewproof.html",{'image':image})
    else:
        return redirect("/xadmin/login")



def deleteProof(request,username):
    tempProof.objects.filter(name__iexact=username).delete()
    proofs = tempProof.objects.all().values('name').annotate(dcount=Count('name')).order_by()
    return render (request,"admin.html",{'deleted':1,'proofs':proofs})



def adminLogin(request):
    if request.session.has_key('adminId'):
        return redirect("/xadmin")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            username = str(username)
            password = str(password)

            if username == "xadmin" and password == "x1234":
                request.session["adminId"] = username

                return redirect("/xadmin")
            else:
                return render (request,"admin-login.html",{'flag':1})
        return render(request,"admin-login.html",{})


def logout(request):
    request.session.flush()
    return redirect("/xadmin/login")



    
