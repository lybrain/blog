from django.db import models
from datetime import datetime
from user.models import User



def article_directory_path(instance, filename):
    return 'article/{0}/{1}'.format(datetime.today().strftime('%Y-%m-%d'), filename)

class Article(models.Model):
     title = models.CharField(max_length=100)
     short_description = models.CharField(max_length=300, null=True)
     description = models.CharField(max_length=2000)
     image = models.ImageField(upload_to=article_directory_path, null=True)
     views = models.PositiveBigIntegerField(default=0)
     user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='articles')
     created_date = models.DateTimeField(auto_now_add=True)
     updated_date = models.DateTimeField(auto_now=True)
     
     
     def __str__(self) -> str:
         return self.title
     
         
     def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete()
        print('hello')
        super().delete(*args, **kwargs)
