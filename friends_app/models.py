from django.db import models

from user_app.models import User

class Friendship(models.Model):
    status = models.CharField(max_length=50, default = "pending")
    from_user = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'sent_friendships')
    to_user = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'received_friendships')
    created_at = models.DateTimeField(auto_now_add= True)  
    
    class Meta:
        unique_together = ('from_user', 'to_user')