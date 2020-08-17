from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", verbose_name="Autor")
    title = models.TextField(max_length=100, verbose_name="Tytuł")
    content = models.TextField(verbose_name="Treść posta")
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-creation_date",)
    
    def __str__(self):
        return f"Post from {self.author}"

class BlogComment(models.Model):
    author = author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments", verbose_name="Autor")
    content = models.TextField(verbose_name="Treść komentarza")
    creation_date = models.DateTimeField(auto_now_add=True)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="comments", verbose_name="Post")

    class Meta:
        ordering = ("-creation_date",)

    def __str__(self):
        return f"Comment from {self.author} on {self.blog_post}"
