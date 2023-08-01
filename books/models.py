from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    genre = models.CharField(max_length=20)
    publication_date = models.DateField()
    price = models.FloatField()
    
    def __str__(self):
        return self.title