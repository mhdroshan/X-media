from django.db import models

# Create your models here.
class Tagmodel(models.Model):
    tag_title=models.CharField(max_length=40,default=0)
    tag_name=models.CharField(max_length=40)
    tag_image=models.ImageField()
    tag_disc=models.TextField(default=0)
    t_country=models.CharField(max_length=20,default=0)
    t_state=models.CharField(max_length=20,default=0)
    t_place=models.CharField(max_length=20,default=0)

    

    def __str__(self):
        return self.tag_title+" "+self.tag_name+" "+self.tag_disc+" "+self.t_country+" "+self.t_state+" "+self.t_place
