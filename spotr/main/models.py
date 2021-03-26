from django.db import models

# Create your models here.

class instagram_data(models.Model):
    name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    private = models.CharField(max_length=20)
    bio = models.CharField(max_length=400)
    follower = models.IntegerField()
    following = models.IntegerField()
    posts =  models.IntegerField()
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name

        


