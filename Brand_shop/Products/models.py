from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300, null=True, blank=True)
    price = models.IntegerField()
    count = models.IntegerField()
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name