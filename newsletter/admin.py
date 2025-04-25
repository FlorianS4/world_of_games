from django.contrib import admin
from .models import Newsletter


class NewsLetterAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'id',
    )


admin.site.register(Newsletter, NewsLetterAdmin)
