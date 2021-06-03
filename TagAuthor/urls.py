from django.urls import path
from TagAuthor import views


app_name="TagAuthor"
urlpatterns = [
    path('',views.home,name="index"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('insert/',views.insert,name="insert"),
    path('delete/<int:id>',views.delete,name="delete"),
   
    
   

]