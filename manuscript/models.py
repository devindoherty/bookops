from django.db import models
from bookops.models import User


# Create your models here.
class Manuscript(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="manuscripts")
    # sender = models.ForeignKey("User", on_delete=models.PROTECT, related_name="emails_sent")
    # recipients = models.ManyToManyField("User", related_name="emails_received")
    title = models.CharField(max_length=255)
    synopsis = models.CharField(max_length=255)
    body = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    accepted = models.BooleanField(default =False)
    
    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "synopsis": self.synopsis,
            "body": self.body,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p"),
            "read": self.read,
            "accepted": self.accepted
        }