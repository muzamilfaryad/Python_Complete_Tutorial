from django.contrib import admin

# Register your models here.
from .models import Color , Person
#to make our Django models visible and manageable in the Django Admin Panel.
admin.site.register(Color)
admin.site.register(Person)