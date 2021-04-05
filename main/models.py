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
    
class codeforces_data(models.Model):
    first_name = models.CharField(max_length=200,null=True)
    last_name = models.CharField(max_length=200,null=True) 
    handle = models.CharField(max_length=200,null=True)
    organisation = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200,null=True)
    country = models.CharField(max_length=200,null=True)
    reg_time = models.CharField(max_length=200,null=True)
    last_online = models.CharField(max_length=200,null=True)
    rating = models.IntegerField(null=True)
    max_rating = models.IntegerField(null=True)
    friends = models.IntegerField(null=True)
    rank = models.CharField(max_length=200,null=True)
    max_rank = models.CharField(max_length=200,null=True)
    link = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.handle


class github_data(models.Model):
    name  = models.CharField(max_length=200,null=True)
    login = models.CharField(max_length=200,null=True)
    bio = models.CharField(max_length=200,null=True)
    location = models.CharField(max_length=200,null=True)
    followers = models.IntegerField(null=True)
    following = models.IntegerField(null=True)
    public_repos = models.IntegerField(null=True)
    created_at =  models.CharField(max_length=200,null=True)
    updated_at = models.CharField(max_length=200,null=True)
    link = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.login

class twitter_data(models.Model):
    name  = models.CharField(max_length=200,null=True)
    screen_name = models.CharField(max_length=200,null=True)
    description = models.CharField(max_length=200,null=True)
    location = models.CharField(max_length=200,null=True)
    follower_count =  models.CharField(max_length=200,null=True)
    friend_count =  models.CharField(max_length=200,null=True)
    created_at =  models.CharField(max_length=200,null=True)
    verified =  models.CharField(max_length=200,null=True)
    last_tweet_time =  models.CharField(max_length=200,null=True)
    last_tweet =  models.CharField(max_length=200,null=True)
    link = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.screen_name
        
class reddit_data(models.Model):
    name = models.CharField(max_length=200,null=True)
    display_name = models.CharField(max_length=200,null=True) 
    verified = models.CharField(max_length=200,null=True)
    is_gold = models.CharField(max_length=200,null=True)
    total_karma = models.CharField(max_length=200,null=True)
    created_utc = models.CharField(max_length=200,null=True)
    icon_img = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name


