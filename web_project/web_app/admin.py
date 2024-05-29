from django.contrib import admin
from .models import Surmodel,Catalog
# Register your models here.

#@admin.register(Surmodel)
@admin.register(Catalog)
class Catalogdmin(admin.ModelAdmin):
    list_display = ("name", "desc")


