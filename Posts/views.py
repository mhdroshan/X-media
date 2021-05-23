from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponse
from .models import PostModel,PostImageModel
from Tags.models import Tagmodel
from User.models import UserModel


def allpost(request):
    posts=PostModel.objects.all()
    return render (request,"index.html",{'posts':posts})

def postdetails(request,id):
    PostImageRecords=PostImageModel.objects.filter(post=id)
    postdetails=PostModel.objects.get(id=id)
    return render(request,"postdetails.html",{"imageRecords":PostImageRecords ,"post":postdetails})


def relatedpost(request,id):
    posts=PostModel.objects.filter(tag_id = id)
    return render (request,"relatedpost.html",{'posts':posts})
    

def addpost(request,id):
    if request.session.has_key('userid'):
        tag=Tagmodel.objects.get(id=id)
        if request.method == 'POST' and request.FILES:
            p=PostModel()
            p.p_title= request.POST.get("posttitle")
            p.p_content= request.POST.get("postdesc")
            p.p_coverimage=request.FILES.get("postimages")
            
            tagObject=Tagmodel.objects.get(id=id)
            p.tag_id=tagObject

            userObject=UserModel.objects.get(id=request.session["userid"])
            p.user_id=userObject
            
            p.save()
            return render (request,"postentry.html",{'tag':tag , 'flag':1})
        
        
        return render (request,"postentry.html",{'tag':tag})
    else:
        return redirect("/user/login")




# def postimages(request,id):
#     allPostImages=PostImageModel.objects.filter(post=id)
#     if request.session.has_key('userid'):
#         if request.method == 'POST' and request.FILES:
#             postImagesObj=PostImageModel()
#             postImagesObj.img_title= request.POST.get("txtCaption")
#             postImagesObj.post_image= request.FILES.get("postImage")

#             postObj=PostModel.objects.get(id=id)
#             postImagesObj.post=postObj

#             # return HttpResponse("Saved")
#             postImagesObj.save()
#             return redirect("/my-posts/")
#         else:
#             return render(request,"postimages.html",{"allPostImages":allPostImages})
        

