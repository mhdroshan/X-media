from django.urls import path
from MasterEntry import views



app_name="adminpanel"
urlpatterns = [
    path('',views.admiHome,name="admin-home"),
    path('login',views.adminLogin,name="admin-login"),
    path('logout',views.logout,name="logout"),
    path('insert',views.insert,name="insert"),
    path('verified/<int:id>',views.userVerify,name="verify"),
    path('proofs/<str:username>',views.ProofDetail,name="Proof-detail"),
  
]