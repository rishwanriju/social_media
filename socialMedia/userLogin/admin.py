from django.contrib import admin
from . import models


admin.site.register(models.dlogin),
admin.site.register(models.Post)
admin.site.register(models.post_like)
admin.site.register(models.post_comment)
