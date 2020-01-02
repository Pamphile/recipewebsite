from django.db import models


class Recipe(models.Model):
    recipe_title = models.CharField(max_length=200)
    recipe_content = models.TextField()
    recipe_published = models.DateTimeField('date published')

    def __str__(self):
        return self.recipe_title