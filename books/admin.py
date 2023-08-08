from django.contrib import admin
from .models import Books, Authors, Publishers, Genres

# Define custom ModelAdmin classes for each model
class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publication_date', 'price', 'authors_list', 'genres_list', 'publishers_list')
    
    def authors_list(self, obj):
        return ', '.join([author.name for author in obj.author.all()])
    authors_list.short_description = 'Authors'
    
    def genres_list(self, obj):
        return ', '.join([genre.name for genre in obj.genre.all()])
    genres_list.short_description = 'Genres'

    def publishers_list(self, obj):
        return ', '.join([publisher.name for publisher in obj.publisher.all()])
    publishers_list.short_description = 'Publishers'

    list_filter = ('publication_date', 'genre', 'author', 'publisher')
    ordering = ["title", 'price']


class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'books_list', 'birthday', 'email')
    def books_list(self, obj):
        return ', '.join([book.title for book in obj.books_authored.all()])
    books_list.short_description = 'Books Written'
    ordering = ["name"]


class PublishersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'books_list', 'founding', 'operational')
    def books_list(self, obj):
        return ', '.join([book.title for book in obj.books_published.all()])
    books_list.short_description = 'Books Published'
    ordering = ["name"]
    list_filter = ['operational']



class GenresAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'books_list', 'description')
    def books_list(self, obj):
        return ', '.join([book.title for book in obj.book_list.all()])
    books_list.short_description = 'Books'
    ordering = ["name"]


# Register your models using the custom ModelAdmin classes
admin.site.register(Books, BooksAdmin)
admin.site.register(Authors, AuthorsAdmin)
admin.site.register(Publishers, PublishersAdmin)
admin.site.register(Genres, GenresAdmin)



