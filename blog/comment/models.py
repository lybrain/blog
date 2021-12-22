from django.db import models
from article.models import Article


class Comment(models.Model):
     name = models.CharField(max_length=100, null=True, blank=True)
     text = models.CharField(max_length=300)
     article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
     created_date = models.DateTimeField(auto_now_add=True)
     class Meta:
        ordering = ['-created_date']