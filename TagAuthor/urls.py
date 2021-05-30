from django.urls import path
from TagAuthor import views


app_name="TagAuthor"
urlpatterns = [
    path('home/',views.home,name="index"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
   
    
   

]