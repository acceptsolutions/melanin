from django.db import models

class Selfcare(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    post = models.BooleanField(default=False)

    def __str__(self):
        return self.title
