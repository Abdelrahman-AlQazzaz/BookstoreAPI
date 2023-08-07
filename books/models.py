from django.db import models

class Authors(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null = True, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name  
      
class Genres(models.Model):
    name = models.SlugField(max_length=100)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name 
    
class Publishers(models.Model):
    name = models.CharField(max_length=200)
    founding = models.DateField(null=True, blank=True)
    operational = models.BooleanField(default=True)

    def __str__(self):
        return self.name 
    
class Books(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField(auto_now_add=True)
    price = models.FloatField(default=10.0)

    author = models.ManyToManyField(Authors, related_name='books_authored')
    genre = models.ManyToManyField(Genres, related_name='book_list')
    publisher = models.ManyToManyField(Publishers, related_name='books_published')

    def __str__(self):
        return self.title
    
