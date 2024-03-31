from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Print(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='prints/')
    price = models.DecimalField(max_digits=10, decimal_places=2)

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