from django.db import models
from django.conf import settings

from user_app.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(
        to = settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE,
        related_name= 'posts'
    )
    
    title = models.CharField(max_length= 150)
    topic = models.CharField(max_length= 120, blank= True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    
    tags = models.ManyToManyField(
        to= 'Tag', 
        related_name= 'posts',
        blank= True,
    ) 
    
    def __str__(self):
        return self.title
    
class Tag(models.Model):
    name = models.CharField(max_length= 50, unique= True)
    
    def __str__(self):
        return self.name

class PostImage(models.Model):
    """
    
    """
    original_image = models.ImageField()
    compressed_image = models.ImageField()


    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class PostLike(models.Model):
    """

    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    

class PostHeart(models.Model):
    """

    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
class PostLink(models.Model):
    """
    
    """
    url = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class PostView(models.Model):
    """
    
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

