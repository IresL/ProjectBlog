from unittest.util import _MAX_LENGTH
from django.db import models
from users.models import User

# Create your models here.
#orm ბაზაში დატას ინახავს კლასებად
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    
class Comment(models.Model):    
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    text = models.TextField()
