from django.urls import path
from Posts import views

from Posts.views import allpost


app_name="Posts"
urlpatterns = [
    path('home/',views.allpost,name="index"),
    path('post-details/<int:id>/',views.postdetails,name="post-details"),
    path('post-entry/<int:id>/',views.addpost,name="post-entry"),
    # path('post-images/<int:id>',views.postimages,name="post-images"),
    path('related-post/<int:id>',views.relatedpost,name="related-post"),


]