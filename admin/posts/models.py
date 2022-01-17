from django.db import models


class Post(models.Model):
    class Meta:
        db_table: str = 'posts'

    title = models.CharField(max_length=50)
    image = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    likes = models.IntegerField(default=0)


# Only need User ID for this model
class User(models.Model):
    pass
