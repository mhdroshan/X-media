from django.urls import path
from User import views


app_name="User"
urlpatterns = [
    path('profile/',views.userprofile,name="profile"),
    path('login/',views.login,name="user-login"),
    path('create/',views.create,name="create"),
    path('ver-name/',views.verName,name="ver-name"),
    path('ver-other/',views.verOther,name="ver-other"),
    path('ver-loc/',views.verLocation,name="ver-loc"),
    path('ver-pla/',views.verPlaceget,name="ver-pla"),
    path('ver-pladd/',views.verPladd,name="ver-pladd"),
    path('ver-dp/',views.verDP,name="ver-dp"),
    path('logout/', views.logout, name='logout'),
    path('tag-req',views.tagreq,name="tagreq"),
    path('moreimage/<int:id>',views.moreimage,name="moreimage"),
    path('change-view/<int:id>',views.changePrivacy,name="change"),
    path('delete/<int:id>',views.deletePost,name="delete"),
    
   

]