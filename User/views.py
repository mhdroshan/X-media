from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import UserModel
from Tags.models import TagRequest
from Posts.models import PostModel,PostImageModel

# Create your views here.

def userprofile(request):
    if request.session.has_key('userid'):
        userid = request.session['userid']
        users=UserModel.objects.get(id=userid)
        allMyPosts=PostModel.objects.filter(user_id=userid)
        return render(request,"User/Profile.html",{'user':users , 'mypost':allMyPosts})
    else:
        return redirect("/user/login")

def changePrivacy(request,id):
    user  = UserModel.objects.get(id=id)
    radio = request.POST.get("anontype")
    if request.method == 'POST':
        if radio == '0':
            
            user.u_security ='0'
            user.save()
            return redirect('User:profile')
            
        elif radio =='1':
            user.u_security = '1'
            user.save()
            return redirect('User:profile')





def moreimage(request,id):
    userid = request.session['userid']
    users=UserModel.objects.get(id=userid)
    allMyPosts=PostModel.objects.filter(user_id=userid)
    if request.method == 'POST' and request.FILES:
        postImagesObj=PostImageModel()
        # postImagesObj.img_title= "image-title"
        postImagesObj.img_title= request.POST.get("imagetitle")
        postImagesObj.post_image= request.FILES.get("postImage")
        postObj=PostModel.objects.get(id=id)
        postImagesObj.post=postObj
        # return HttpResponse(postImagesObj)
        postImagesObj.save()
        return render(request,"User/Profile.html",{'flag':1 ,'user':users,'mypost':allMyPosts})

    else:
        return render(request,"User/Profile.html",{'user':users,'mypost':allMyPosts})
    
    
def login(request):
    if request.session.has_key('userid'):
        return redirect("/user/profile")
    else:
        if request.method=="POST":
            userLoged=UserModel.objects.filter(u_username=request.POST.get("username"),u_pass=request.POST.get("password")).count()
            if userLoged>0:
                user=get_object_or_404(UserModel, u_username=request.POST.get("username"),u_pass=request.POST.get("password"))
                request.session["userid"]=user.id
                return redirect("/")
            else:
                return render(request,"user/login.html",{'fail':1})
        return render(request,"user/login.html",{})



def logout(request):
    request.session.flush()
    return redirect("/user/login")


def tagreq(request):
    if request.session.has_key('userid'):
        
        if request.method=="POST":
            t=TagRequest()
            t.tr_title=request.POST.get("tagtitle")
            t.tr_content=request.POST.get("tagdesc")
            t.tr_c=request.POST.get("tagcountry")
            t.tr_s=request.POST.get("tagstate")
            t.tr_p=request.POST.get("tagplace")
            t.tr_type=request.POST.get("loctype")

            userObject=UserModel.objects.get(id=request.session["userid"])
            t.user_id=userObject
            
            

            t.save()
            return render(request,"user/tagRequest.html",{'flag':1})
        return render(request,"user/tagRequest.html",{})

    else:
        return redirect("/user/login")

