from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50, null=True)
    description = models.TextField()
    cover = models.FileField(upload_to='covers', null=True, blank=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
