from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        # This is to correct django's defualt behaviour of appending an 's' to the end of classes for plural spelling
        verbose_name_plural = "categories"

    # Set to for better string representation
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")

    def __str__(self):
        return self.title