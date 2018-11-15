from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin ):
    list_display = ('nameContact', 'email', 'phone', 'message')
    search_fields = ['nameContact']

admin.site.register(Contact, ContactAdmin)
