from django.db import models
from User.models import UserModel
from Tags.models import Tagmodel

# Create your models here.

class PostModel(models.Model):
    p_title=models.CharField(max_length=50,null=True)
    p_content=models.TextField()
    p_coverimage=models.ImageField(upload_to="coverimage",null=True)
    pos_votes =models.IntegerField(default=0)
    neg_votes=models.IntegerField(default=0)
    p_score=models.IntegerField(default=0)
    p_dateTime =models.DateTimeField(auto_now=True)
    
    user_id=models.ForeignKey(UserModel,on_delete=models.SET_NULL,null=True,verbose_name="UserModel")
    tag_id=models.ForeignKey(Tagmodel,on_delete=models.SET_NULL,null=True,verbose_name="Tagmodel")
    
    def __str__(self):
        return self.p_title
    
     

class PostImageModel(models.Model):
    img_title=models.CharField(max_length=50,null=True)
    post_image=models.ImageField(upload_to='post_images')
    p_dateTime =models.DateTimeField(auto_now=True)
    post=models.ForeignKey(PostModel,on_delete=models.SET_NULL,null=True)

    def __str__(self):
            return self.img_title