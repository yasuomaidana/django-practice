from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    roles = models.TextField(null=True, blank=True)

    objects = models.Manager()

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username
