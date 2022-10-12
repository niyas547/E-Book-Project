from django.contrib import admin
from api.models import Genre,Books,Review

# Register your models here.
admin.site.register(Genre)
admin.site.register(Books)
admin.site.register(Review)
