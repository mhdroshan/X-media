from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
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

        # Use u_selected_nearby_city if available, otherwise fallback to u_detected_city
        if user.u_selected_nearby_city:
            ptags = Tagmodel.objects.filter(t_place__iexact=user.u_selected_nearby_city)
        elif user.u_detected_city:
            ptags = Tagmodel.objects.filter(t_place__iexact=user.u_detected_city)
        else:
            ptags = Tagmodel.objects.none() # No place information available

        return render(request, "alltags.html",{'ctags':ctags ,'stags':stags ,'ptags':ptags , 'user':user})
       
    else:
        return redirect("/user/login")

def findTags(request):
    if request.session.has_key('userid'):
        loggeduser = UserModel.objects.get(id = request.session['userid'])
        tags = Tagmodel.objects.all()
        users_tag = following.objects.filter(user = loggeduser)
        followed_tags_ids = [f.tag.id for f in users_tag] # Get IDs of tags the user follows
        country = PostModel.objects.all().values('tag_id__t_country').annotate(dcount=Count('tag_id__t_country')).order_by()
        # user-tags = PostModel.objects.all().values('user_id__t_country').annotate(gcount=Count('tag_id__t_country')).order_by()
        users = UserModel.objects.all()

        # return HttpResponse(mytag)
        return render(request, "find-tags.html",{
            'users':users,
            "tags":tags,
            "country":country,
            "u_tags":users_tag,
            "followed_tags_ids": followed_tags_ids, # Pass the list of followed tag IDs
        })

    else:
        return redirect("/user/login")


def followtag(request):
    if not request.session.has_key('userid'):
        return JsonResponse({'success': False, 'message': 'User not logged in.'}) # Return JSON for AJAX

    if request.method == "POST":
        try:
            tag_id = request.POST.get('tag_id')
            if not tag_id:
                return JsonResponse({'success': False, 'message': 'Tag ID is required.'})
            
            tag = get_object_or_404(Tagmodel, id=tag_id)
            user = UserModel.objects.get(id=request.session['userid'])
            is_followed = False

            if following.objects.filter(tag=tag, user=user).exists():
                # Unfollow
                current_fol = following.objects.filter(tag=tag).count()
                following.objects.filter(tag=tag).update(follow_count=F("follow_count") - 1)
                following.objects.get(tag=tag, user=user).delete()
                message = 'Tag unfollowed.'
                is_followed = False
            else:
                # Follow
                foll = following(tag=tag, user=user, is_follow=1)
                foll.save()
                current_fol = following.objects.filter(tag=tag).count()
                following.objects.filter(tag=tag).update(follow_count=F("follow_count") + 1)
                message = 'Tag followed.'
                is_followed = True

            return JsonResponse({'success': True, 'message': message, 'is_followed': is_followed})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}) # Return specific error message
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method.'})
