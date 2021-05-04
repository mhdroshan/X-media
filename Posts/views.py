from django.shortcuts import render
from django.http import HttpResponse
from .models import PostModel


def allpost(request):

    posts=PostModel.objects.all()
    return render (request,"index.html",{'posts':posts})