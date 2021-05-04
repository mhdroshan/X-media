from django.shortcuts import render
from django.http import HttpResponse
from .models import Tagmodel
# Create your views here.


def alltags(request):

    tags=Tagmodel.objects.all()
    return render(request, "alltags.html",{'tags':tags})
