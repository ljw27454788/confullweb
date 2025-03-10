from django.contrib import admin
from web.models import *

# Register your models here.
@admin.register(Product)
class Product(admin.ModelAdmin):
    readonly_fields = ('id',)
    pass

@admin.register(News)
class News(admin.ModelAdmin):
    readonly_fields = ('id',)
    pass