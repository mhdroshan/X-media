from django.db import models

# Create your models here.

class UserModel(models.Model):
    u_name=models.CharField(max_length=20,null=False)
    u_pass=models.CharField(max_length=20,null=True)
    u_username=models.CharField(max_length=20,null=True)
    u_age=models.IntegerField()
    u_pic=models.ImageField(upload_to='user_dp')
    u_country= models.CharField(max_length=20,default=0)
    u_state=models.CharField(max_length=20,default=0)
    u_place=models.CharField(max_length=20,default=0)
    u_security=models.BooleanField(default=0)

    def __str__(self):
        return self.u_name+" "+self.u_country+" "+self.u_state+" "+self.u_place