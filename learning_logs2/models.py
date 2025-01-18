from django.db import models


# Create your models here.

class Topic2(models.Model):
    topic = models.CharField(max_length=200)
    added_date = models.DateTimeField(auto_now_add=True)


def __str__(self):
    """Return a string representation of the model."""
    return self.text
