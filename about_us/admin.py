from django.contrib import admin
from .models import AboutUs, ContactUs


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    """
    Display contact us message on admin page.
    """
    list_display = ('name', 'email', 'contact_description', 'created_on')
    search_fields = ('name', 'email', 'contact_description')
    list_filter = ('name', 'email')


admin.site.register(AboutUs)