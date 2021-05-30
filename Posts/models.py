from django.db import models
from User.models import UserModel
from Tags.models import Tagmodel

# Create your models here.

class PostModel(models.Model):
    p_title=models.CharField(max_length=50,null=True)
    p_content=models.TextField()
    p_coverimage=models.ImageField(upload_to="coverimage",null=True)
    pvoted = models.ManyToManyField(UserModel , default=None , blank=True ,related_name='pvoted')
    nvoted = models.ManyToManyField(UserModel , default=None , blank=True ,related_name='nvoted')
    p_score=models.IntegerField(default=0)
    p_dateTime =models.DateTimeField(auto_now=True)
    
    user_id=models.ForeignKey(UserModel,on_delete=models.SET_NULL,null=True,verbose_name="UserModel")
    tag_id=models.ForeignKey(Tagmodel,on_delete=models.SET_NULL,null=True,verbose_name="Tagmodel")
    
    def __str__(self):
        return self.p_title
    
    @property
    def p_num_votes(self):
         return self.pvoted.all().count()
    @property
    def n_num_votes(self):
         return self.nvoted.all().count()


VOTE_CHOICES=(
    ('Yes','Yes'),
    ('No','No'),
)



class PositiveVote(models.Model):
    user = models.ForeignKey(UserModel , on_delete=models.Case)
    post = models.ForeignKey(PostModel , on_delete=models.Case)
    value = models.CharField(choices = VOTE_CHOICES ,default='Yes',max_length=20)

    def __str__(self):
        return str(self.post)


class NegativeVote(models.Model):
    user = models.ForeignKey(UserModel , on_delete=models.Case)
    post = models.ForeignKey(PostModel , on_delete=models.Case)
    value = models.CharField(choices = VOTE_CHOICES ,default='Yes',max_length=20)

    def __str__(self):
        return str(self.post)

class PostImageModel(models.Model):
    img_title=models.CharField(max_length=50,null=True)
    post_image=models.ImageField(upload_to='post_images')
    p_dateTime =models.DateTimeField(auto_now=True)
    post=models.ForeignKey(PostModel,on_delete=models.SET_NULL,null=True)

    def __str__(self):
            return self.img_title