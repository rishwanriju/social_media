from django.db import models
from datetime import datetime

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


# class Posts(models.Model):
#     STATUS = (
#     (0,"Draft"),
#     (1,"Publish")
# )

# class Post(models.Model):
#     slug = models.SlugField(max_length=200, unique=True)
#     author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='posts')
#     updated_on = models.DateTimeField(auto_now= True)
#     content = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     status = models.IntegerField(choices=STATUS, default=0)

#     class Meta:
#         ordering = ['-created_on']


