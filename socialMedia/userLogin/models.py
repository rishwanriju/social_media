from django.db import models
from datetime import datetime
from stream_django.activity import Activity
from django.conf import settings
from django.urls import reverse



class dlogin(models.Model):
    gender = (
        ('male','m'),
        ('female','f')
    )
    
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=10,
    choices=gender)
    date_subscribed = models.DateTimeField(default=datetime.now())
    messages_received = models.IntegerField(default=0)



    #    **----------------------------------------------------------------**


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    author = models.ForeignKey(dlogin, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    posts = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.posts

    def get_absolute_url(self):
        return reverse('Posts')




