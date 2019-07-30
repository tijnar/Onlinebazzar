from django.db import models

# Create your models here.
from sorl.thumbnail import ImageField


class Banner(models.Model):
    image = ImageField()
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    button_text = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Menu(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.title

