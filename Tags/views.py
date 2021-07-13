from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Tagmodel, following
from django.db.models import Count , F
from Posts.models import PostModel
from User.models import UserModel
import json

# Create your views here.


def alltags(request):
    if request.session.has_key('userid'):
        user=UserModel.objects.get(id=request.session['userid'])
        ctags=Tagmodel.objects.filter(t_country__iexact=user.u_country)
        stags=Tagmodel.objects.filter(t_state__iexact=user.u_state)
        ptags=Tagmodel.objects.filter(t_place__iexact=user.u_place)
        return render(request, "alltags.html",{'ctags':ctags ,'stags':stags ,'ptags':ptags , 'user':user})
       
    else:
        return redirect("/user/login")

def findTags(request):
    if request.session.has_key('userid'):
        loggeduser = UserModel.objects.get(id = request.session['userid'])
        tags = Tagmodel.objects.all()
        users_tag = following.objects.filter(user = loggeduser)
        country = PostModel.objects.all().values('tag_id__t_country').annotate(dcount=Count('tag_id__t_country')).order_by()
        # user-tags = PostModel.objects.all().values('user_id__t_country').annotate(gcount=Count('tag_id__t_country')).order_by()
        users = UserModel.objects.all()

        # return HttpResponse(mytag)
        return render(request, "find-tags.html",{
            'users':users,
            "tags":tags,
            "country":country,
            "u_tags":users_tag,
        })

    else:
        return redirect("/user/login")


def followtag(request,id):    
    
    tag = Tagmodel.objects.get(id=id)
    if request.session.has_key('userid'):
        user =UserModel.objects.get(id = request.session['userid'])
        
        foll = following()
        use = UserModel()
        foll.tag=tag
        if following.objects.filter(tag = id,user = user).count() > 0:
            current_fol = following.objects.filter(tag = id).count()
            following.objects.filter(tag = id).update(follow_count = current_fol-1)
            following.objects.get(tag__id = id,user = user ).delete()

            
        else:

            foll.user = user  
            # foll.follow_count =F("follow_count")+1
            foll.is_follow = 1
            current_fol = following.objects.filter(tag = id).count()
            foll.save()
            following.objects.filter(tag = tag).update(follow_count = current_fol+1)
            # following.objects.filter(tag = tag).update(follow_count = F("follow_count")+1)

            


        return redirect("Posts:related-post" , id=id)

    else:
        return redirect("/user/login")
