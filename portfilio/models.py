from django.db import models


# Create your models here.


class Message(models.Model):
    Username = models.CharField(max_length=1000)
    Email = models.CharField(max_length=500)
    Subject = models.CharField(max_length=500)
    Message = models.TextField()
    id = models.IntegerField(primary_key=True, editable=False, unique=True)

    def __str__(self):
        return str(self.Username) + " Sent " + str(self.Subject)
