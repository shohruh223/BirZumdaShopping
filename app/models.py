from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Category(models.Model):
    title = models.CharField()

    def __str__(self):
        return self.title


class Product(models.Model):
    image = models.ImageField()
    category = models.ForeignKey(to='Category',
                                 on_delete=models.CASCADE)
    title = models.CharField()
    text = models.TextField()
    rating = models.IntegerField(default=1,
                                 validators=[MinValueValidator(1), MaxValueValidator(5)])
    price = models.DecimalField(max_digits=9, decimal_places=2)
    is_have = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
