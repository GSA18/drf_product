from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self) -> str:
        return f'{self.name}'


class Color(models.Model):
    name = models.CharField(max_length=15, null=False, blank=False)

    def __str__(self) -> str:
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=3, null=False)
    altura = models.DecimalField(max_digits=4, decimal_places=2, null=False)
    largura = models.DecimalField(max_digits=4, decimal_places=2, null=False)
    peso = models.DecimalField(max_digits=4, decimal_places=2, null=False)
    categories = models.ManyToManyField(Category)
    color = models.ManyToManyField(Color)

    def __str__(self) -> str:
        return f'{self.name}'
