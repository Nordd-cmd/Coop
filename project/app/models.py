from django.db import models


class DNS_Shop(models.Model):
    title = models.CharField(max_length=20)
    number = models.IntegerField()
    creator = models.CharField(max_length=20)
    about = models.TextField(max_length=500)
    price = models.IntegerField()

    def __str__(self):
        return self.title

