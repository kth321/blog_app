from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50, null=True)
    body = models.TextField()
    photo = models.ImageField(null=True, blank=True)
    published_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.title
