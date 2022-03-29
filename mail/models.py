
from django.db import models


# Create your models here.

class emails(models.Model):
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=250)
    from_email = models.EmailField()
    receiver_one = models.EmailField()
    receiver_two = models.EmailField(default=None)
    receiver_three = models.EmailField(default=None)
    receiver_four = models.EmailField(default=None)
    receiver_five = models.EmailField(default=None)
    cc_myself = models.EmailField()
    
    
    def __str__(self):
        return self.subject