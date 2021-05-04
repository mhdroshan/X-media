from django.db import models

# Create your models here.

class PostModel(models.Model):
    p_title=models.CharField(max_length=50,default=0)
    p_content=models.TextField()
    pos_votes =models.IntegerField()
    neg_votes=models.IntegerField()
    p_score=models.IntegerField()
    p_dateTime =models.DateTimeField(auto_now=True)

    # images username tagname


    def __str__(self):
        return self.p_title+" "+self.p_content