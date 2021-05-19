from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Tagmodel

from User.models import UserModel

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


