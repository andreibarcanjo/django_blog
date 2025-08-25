from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    data_pub = models.DateTimeField(auto_now_add=True)
    references = models.TextField(blank=True, null=True)
    attachments = models.FileField(
        upload_to='attachments/', blank=True, null=True)
    pass
