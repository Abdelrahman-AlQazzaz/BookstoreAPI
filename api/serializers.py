from rest_framework import serializers
from books.models import Books, Authors, Genres, Publishers

class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ("id","title")

class BookSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(many=True, queryset=Authors.objects.all(), slug_field='name')
    genre = serializers.SlugRelatedField(many=True, queryset=Genres.objects.all(), slug_field='name')
    publisher = serializers.SlugRelatedField(many=True, queryset=Publishers.objects.all(), slug_field='name')

    class Meta:
        model = Books
        fields = ('id', 'title', 'author', 'genre', 'publisher', 'publication_date', 'price')
    
    def create(self, validated_data):
        # Extract the author, genre, and publisher data from the validated data
        authors_data = validated_data.pop('author', [])
        genres_data = validated_data.pop('genre', [])
        publishers_data = validated_data.pop('publisher', [])

        # Create or retrieve the related Author instances
        authors = []
        for author_data in authors_data:
            author, _ = Authors.objects.get_or_create(name=author_data)
            authors.append(author)

        # Create or retrieve the related Genre instances
        genres = []
        for genre_data in genres_data:
            genre, _ = Genres.objects.get_or_create(name=genre_data)
            genres.append(genre)

        # Create or retrieve the related Publisher instance
        publishers = []
        for publisher_data in publishers_data:
            publisher, _ = Publishers.objects.get_or_create(name=publisher_data)
            publishers.append(publisher)

        # Create the Book instance with the related objects
        book = Books.objects.create(**validated_data)

        # Add the related objects to the Many-to-Many fields of the Book instance
        book.author.set(authors)
        book.genre.set(genres)
        book.publisher.set(publishers)

        return book

class AuthorSerializer(serializers.ModelSerializer):
    books_authored = BookListSerializer(many=True, read_only=True)

    class Meta:
        model = Authors
        fields = ('id', 'name', 'birthday','email', 'books_authored')
        
    """def to_representation(self, value):
         return value.name"""
    
class GenreSerializer(serializers.ModelSerializer):
    book_list = BookListSerializer(many=True, read_only=True)

    class Meta:
        model = Genres
        fields = ('id', 'name', 'description', 'book_list')

class PublisherSerializer(serializers.ModelSerializer):
    books_published = BookListSerializer(many=True, read_only=True)

    class Meta:
        model = Publishers
        fields = ('id','name', 'founding', 'operational', 'books_published')
