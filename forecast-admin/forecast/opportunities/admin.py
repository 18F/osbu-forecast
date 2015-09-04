from django.contrib import admin

# Register your models here.
from .models import Award

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    pass