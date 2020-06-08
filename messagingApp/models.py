from django.db import models


class Message(models.Model):
    sender = models.CharField(max_length=50) #TODO: turn to User later
    receiver = models.CharField(max_length=50) #TODO: turn to User later
    message = models.CharField(max_length=500)
    subject = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
