from django.urls import path
from Tags import views

from Tags.views import alltags


app_name="Tags"
urlpatterns = [
    path('allTags/',views.alltags,name="all-Tags-List"),
    path('findtags/',views.findTags,name="find-Tags"),
    path('follow_toggle/',views.followtag,name="follow_toggle"),
 
    # path('write-post/<int:id>/',views.postimages,name="write-post"),

]