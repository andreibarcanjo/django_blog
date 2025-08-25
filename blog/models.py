from django.db import models

# Create your models here.


class Post(models.model):
    title = models.CharField(max_length=200)
    pass
