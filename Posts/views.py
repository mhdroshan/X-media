from django.db.models.query_utils import Q
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import PostModel,PostImageModel,PositiveVote,NegativeVote,PostComment
from Tags.models import Tagmodel
from User.models import UserModel


def allpost(request):
    posts=PostModel.objects.all().order_by('p_dateTime').reverse()
    return render (request,"index.html",{'posts':posts})

def postdetails(request,id):
    PostImageRecords=PostImageModel.objects.filter(post=id)
    comments = PostComment.objects.filter(post = id).order_by('com_time').reverse()
    postdetails=PostModel.objects.get(id=id)
    return render(request,"postdetails.html",{"imageRecords":PostImageRecords ,"post":postdetails,"comment":comments})


def postvote(request,id):
    if request.session.has_key('userid'):
        uid= request.session["userid"]
        user = UserModel.objects.get(id=request.session["userid"])
        posts=PostModel.objects.filter(~Q(user_id=uid), tag_id = id )

        context = {
            'posts':posts,
            'user':user,
        }
        
        return render (request,"postvote.html",context)
    else:
        return redirect("/user/login")


def posvote(request):
    user = UserModel.objects.get(id=request.session["userid"])
    tag_id = request.POST.get('tag_id')
    if request.method =='POST': 
        post_id = request.POST.get('pos_id')
        post_obj = PostModel.objects.get(id=post_id)

        if user in post_obj.pvoted.all():
            post_obj.pvoted.remove(user)
        else:
            post_obj.pvoted.add(user)

        pvote , pcreated = PositiveVote.objects.get_or_create(user=user,post_id=post_id)  

        if not pcreated:
            if pvote.value=='Yes':
                pvote.value=='No'
            else:
                pvote.value = 'Yes'
        pvote.save()
    return redirect("Tags:all-Tags-List")



# negative vote
def negvote(request):
    user = UserModel.objects.get(id=request.session["userid"])
    if request.method =='POST': 
        post_id = request.POST.get('neg_id')
        post_obj = PostModel.objects.get(id=post_id)

        if user in post_obj.nvoted.all():
            post_obj.nvoted.remove(user)
        else:
            post_obj.nvoted.add(user)

        nvote , ncreated = NegativeVote.objects.get_or_create(user=user,post_id=post_id)
        if not ncreated:
            if nvote.value=='Yes':
                nvote.value=='No'
            else:
                nvote.value = 'Yes'
        nvote.save()
    return redirect("Tags:all-Tags-List")




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


def addcomment(request,id):
    PostImageRecords=PostImageModel.objects.filter(post=id)
    comments = PostComment.objects.filter(post = id).order_by('com_time').reverse()
    postdetails=PostModel.objects.get(id=id)
    if request.session.has_key('userid'):
        if request.method == 'POST':
            PC = PostComment()
            post = PostModel.objects.get(id=id)
            user = UserModel.objects.get(id=request.session["userid"])

            PC.com_data =  request.POST.get("comment")
            PC.post = post
            PC.user = user
            PC.save()

        return render(request,"postdetails.html",{"imageRecords":PostImageRecords ,"post":postdetails ,"comment":comments, "flag":1})

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
        

