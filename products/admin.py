from django.contrib import admin
from .models import GameProduct, Category

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


admin.site.register(GameProduct, GameProductAdmin)
admin.site.register(Category, CategoryAdmin)
