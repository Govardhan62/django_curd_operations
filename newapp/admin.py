from django.contrib import admin
from newapp.models import Member

# Register your models here.
class Display(admin.ModelAdmin):
    list_display ="firstname","lastname","country"

admin.site.register(Member,Display)
