from django.contrib import admin
from .models import GameProduct, Category, Review

# Register your models here.


class GameProductAdmin(admin.ModelAdmin):
    """
    Admin model for managing products
    """
    list_display = (
        'sku',
        'product_name',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'friendly_name',
        'name',
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'reviewer',
        'created_on',
    )


admin.site.register(GameProduct, GameProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
