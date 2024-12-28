from django.db import models


class Author(models.Model):
    author = models.CharField(max_length=20)

    def __str__(self):
        return self.author
class Category(models.Model):
    title = models.CharField(max_length=20)\

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_of_create = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return self.title

