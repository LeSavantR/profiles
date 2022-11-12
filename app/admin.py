from django.contrib import admin

from app.models import Invoice, Item

admin.site.register(Invoice)
admin.site.register(Item)
