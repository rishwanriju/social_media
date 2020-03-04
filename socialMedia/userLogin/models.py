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
    
    username = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50,unique=True)
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
    author = models.ForeignKey(dlogin, on_delete= models.CASCADE,null=True,related_name='post_author')
    updated_on = models.DateTimeField(auto_now= True)
    posts = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    post_like   =   models.IntegerField(default=0)

    
    class Meta:
        ordering = ['-created_on']

class post_like(models.Model):
    user = models.ForeignKey(dlogin,on_delete=models.CASCADE, related_name="post_like") 
    post = models.ForeignKey(Post,on_delete = models.CASCADE, related_name='user_like' )


    def save(self,*arg,**kwarg):
        if not self.pk:
            self.post.post_like+=1
            self.post.save()
            return super().save(arg,**kwarg)
        else:
           
            return self.delete()

    def delete(self):
        self.post.post_like-=1
        self.post.save()
        return super().delete()




