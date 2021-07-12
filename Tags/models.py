from django.db import models
from User.models import UserModel


# Create your models here.
class Tagmodel(models.Model):
    tag_title=models.CharField(max_length=40,default=0)
    tag_name=models.CharField(max_length=40,unique=True)
    tag_image=models.ImageField(upload_to='tags')
    tag_disc=models.TextField(default=0)
    t_country=models.CharField(max_length=20)
    t_state=models.CharField(max_length=20)
    t_place=models.CharField(max_length=20)

    

    def __str__(self):
        return self.tag_name+" "+self.t_country+" "+self.t_state+" "+self.t_place

class TagRequest(models.Model):
    tr_title=models.CharField(max_length=40,default=0)
    tr_type=models.CharField(max_length=10,default=0)
    tr_content=models.TextField(default=0)
    tr_c=models.CharField(max_length=40,default=0)
    tr_s=models.CharField(max_length=40,default=0)
    tr_p=models.CharField(max_length=40,default=0)
    tr_date =models.DateTimeField(auto_now=True,null=False)
    user_id=models.ForeignKey(UserModel,on_delete=models.SET_NULL,null=True,verbose_name="user")

    def __str__(self):
        return self.tr_title+" - "+self.tr_c+" - "+self.tr_s+" - "+self.tr_p
    


class following(models.Model):
    tag = models.ForeignKey(Tagmodel,on_delete=models.SET_NULL,null=True,verbose_name="Tagmodel")
    user = models.ForeignKey(UserModel,on_delete=models.SET_NULL,null=True,verbose_name="UserModel")
    is_follow = models.BooleanField(default=0)
    follow_count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.tag) 