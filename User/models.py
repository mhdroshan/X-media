
from django.db import models

# Create your models here.

class UserModel(models.Model):
    u_name=models.CharField(max_length=20,null=True)
    u_pass=models.CharField(max_length=20,null=False)
    u_username=models.CharField(max_length=20,null=True,unique=True)
    u_email=models.CharField(max_length=20,null=True)
    u_phone=models.CharField(max_length=20,null=True)
    u_age=models.IntegerField()
    u_country= models.CharField(max_length=20,default=0)
    u_state=models.CharField(max_length=20,null=True, blank=True)
    u_latitude=models.CharField(max_length=50, null=True, blank=True) # New: store latitude
    u_longitude=models.CharField(max_length=50, null=True, blank=True) # New: store longitude
    u_detected_city=models.CharField(max_length=50, null=True, blank=True) # New: store detected city
    u_selected_nearby_city=models.CharField(max_length=255, null=True, blank=True) # New: store selected nearby city
    u_security=models.BooleanField(default=0)
    u_verified=models.BooleanField(default=0)

    def __str__(self):
        return f"{self.u_name or ''} {self.u_country or ''} {self.u_state or ''} {self.u_detected_city or ''}".strip()
    


