from django.contrib import admin
from .models import Service

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
    )

    ordering = ('name',)


admin.site.register(Service, ProductAdmin)
