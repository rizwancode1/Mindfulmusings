from django.db import models
from django.contrib.auth.models import User

class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    hashtag = models.CharField(max_length=50)

    def __str__(self):
        return self.hashtag

    def save(self, *args, **kwargs):
        if not self.hashtag.startswith('#'):
            self.hashtag = '#' + self.hashtag
        super().save(*args, **kwargs)




class Article(models.Model):
    image = models.ImageField(null=True, default= "Featured_image.jpg")
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Categories)
    tag = models.ManyToManyField(Tag)
    likes = models.ManyToManyField(User, related_name='liked_articles', blank=True )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"
