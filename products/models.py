from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    """
    Models for product categories
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class GameProduct(models.Model):
    """
    Model for products
    """
    category = models.ForeignKey('Category',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    product_name = models.CharField(max_length=254)
    product_description = models.TextField()
    physical_or_digital = models.BooleanField(default=False,
                                              null=True,
                                              blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6,
                                 decimal_places=2,
                                 null=True,
                                 blank=True)
    image_url = models.URLField(max_length=1024,
                                null=True,
                                blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.product_name


class Review(models.Model):
    """
    Model so a user can leave a review
    """
    product = models.ForeignKey(GameProduct,
                                on_delete=models.CASCADE,
                                related_name="reviews",
                                null=False)
    reviewer = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name='reviewer',
                                 null=False)
    rating = models.DecimalField(max_digits=6,
                                 decimal_places=2,
                                 null=True,
                                 blank=True)
    review_description = models.TextField()
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review {self.review_description} by {self.reviewer}"
