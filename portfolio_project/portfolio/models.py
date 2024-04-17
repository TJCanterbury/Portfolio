from django.db import models
from mdeditor.fields import MDTextField
# from django_markdown.models import MarkdownField

# Create your models here.
class Blog(models.Model):
    """Blog model """
    title = models.CharField(max_length=100)
    # body = MarkdownField()
    body = MDTextField(null=True, blank=True)

    def __str__(self):
        return self.title

class Profile(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Sketches(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='sketches/')

    def __str__(self):
        return self.title

class Print(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='prints/')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

class Images(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='prints/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Images"

    def __str__(self):
        return self.title

class Publications(models.Model):
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    year = models.IntegerField(null=True)

    class Meta:
        verbose_name_plural = "Publications"

    def __str__(self):
        return self.title