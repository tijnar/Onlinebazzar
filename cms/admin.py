from django.contrib import admin

# Register your models here.
from cms.models import Menu, Banner

admin.site.register(Menu)
admin.site.register(Banner)
