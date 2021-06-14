from django.urls import path
from Posts import views

from Posts.views import allpost


app_name="Posts"
urlpatterns = [
    path('',views.allpost,name="index"),
    path('post-details/<int:id>/',views.postdetails,name="post-details"),
    path('post-entry/<int:id>/',views.addpost,name="post-entry"),
    # path('post-images/<int:id>',views.postimages,name="post-images"),
    path('related-post/<int:id>',views.relatedpost,name="related-post"),
    path('related-post2/<int:id>',views.relatedpostUser,name="related-post-user"),
    path('post-vote/<int:id>',views.postvote,name="post-vote"),
    path('addcomment/<int:id>',views.addcomment,name="addcomment"),
    path('pos-vote/',views.posvote,name="pos-vote"),
    path('neg-vote/',views.negvote,name="neg-vote"),


]