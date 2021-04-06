from django.test import TestCase
from main.models import *


class TestModels(TestCase):

    def setUp(self):

        self.reddit = reddit_data.objects.create(
                        name = 'Piyush',
                        total_karma = '123',
                        created_utc = '02-03-2021 04:22:21',
                        icon_img = 'www.google.com'
                        )
        
        self.instagram = instagram_data.objects.create(
                            name = 'mridul',
                            user_name = 'mridul',
                            private = 'yes',
                            bio = 'bio',
                            follower = 100,
                            following = 100,
                            posts =  100,
                            link = 'instagram.com'
                            )

        self.codeforces = codeforces_data.objects.create(
                            first_name = 'piyush',
                            last_name = 'gurjar',
                            handle = 'piyush',
                            organisation = 'iita',
                            city = 'indore',
                            country = 'india',
                            reg_time = 'yesterday',
                            last_online = 'now',
                            rating = 2111,
                            max_rating = 2111,
                            friends = 100,
                            rank = 'newbie',
                            max_rank = 'GM',
                            link = 'codeforces'
                            )

        self.twitter = twitter_data.objects.create(
                        name  = 'mridul',
                        screen_name = 'mridul',
                        description = 'description',
                        location = 'location',
                        follower_count =  '100',
                        friend_count = '122',
                        created_at =  'yesterday',
                        verified =  'yes',
                        last_tweet_time =  'now',
                        last_tweet =  'do it',
                        link = 'twitter'
                        )
        self.github = github_data.objects.create(
                        name  = 'mridul',
                        login = 'mridul',
                        bio = 'bio',
                        location = 'india',
                        followers = 100,
                        following = 100,
                        public_repos = 100,
                        created_at =  'yesterday',
                        updated_at = 'now',
                        link = 'github'
                        )
    
    def test_reddit(self):
        self.assertEquals(self.reddit.name,'Piyush')
        self.assertEquals(self.reddit.total_karma,'123')

    def test_instagram(self):
        self.assertEquals(self.instagram.name,'mridul')
        self.assertEquals(self.instagram.follower,100)

    def test_codeforces(self):
        self.assertEquals(self.codeforces.first_name,'piyush')
        self.assertEquals(self.codeforces.friends,100)

    def test_twitter(self):
        self.assertEquals(self.twitter.name,'mridul')
        self.assertEquals(self.twitter.verified,'yes')
    
    def test_github(self):
        self.assertEquals(self.github.name,'mridul')
        self.assertEquals(self.github.location,'india')