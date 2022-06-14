from django.db import models

# Create your models here.
class Post{models.Model}:
    Title = models.CharField(maxlength = 200)
    Text = models.TextField()
    Author = models.ForeignKey(get_user_model())
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()
