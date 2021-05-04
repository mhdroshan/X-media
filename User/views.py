from django.shortcuts import render
from django.http import HttpResponse
from .models import UserModel
# Create your views here.


def user(request):

    users=UserModel.objects.all()
    return render(request,"User/Profile.html",{'users':users})