from django.db import models

# Create your models here.


class AuthorModel(models.Model):
    a_name = models.CharField(max_length=20,null=False)
    a_pass= models.CharField(max_length=20,null=True)
    a_username=models.CharField(max_length=20,null=True)
    a_loctype=models.CharField(max_length=20,null=True)
    a_location=models.CharField(max_length=50,null=True)
    a_age=models.IntegerField()

    def __str__(self):
        return self.a_name
    