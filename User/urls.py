from django.urls import path
from User import views


app_name="User"
urlpatterns = [
    path('profile/',views.userprofile,name="profile"),
    path('login/',views.login,name="user-login"),
    path('logout/', views.logout, name='logout'),
    path('tag-req',views.tagreq,name="tagreq"),
    path('moreimage/<int:id>',views.moreimage,name="moreimage"),
    path('change-view/<int:id>',views.changePrivacy,name="change"),
    
   

]