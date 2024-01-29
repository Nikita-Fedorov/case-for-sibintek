from django.db import models


class Myself(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self) -> str:
        return self.name
