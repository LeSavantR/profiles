from django.contrib import admin

from app.models import Invoice, Item, Requirements

admin.site.register(Invoice)
admin.site.register(Item)
admin.site.register(Requirements)