from django.urls import path
from Tags import views

from Tags.views import alltags


app_name="Tags"
urlpatterns = [
    path('allTags/',views.alltags,name="all-Tags-List"),
 
    # path('write-post/<int:id>/',views.postimages,name="write-post"),

]