from django.contrib import admin
from .models import *

# Register your models here.
class BoardAdmin(admin.ModelAdmin):
    search_fields = ['subject', 'content']

admin.site.register(Board, BoardAdmin)
admin.site.register(Comment)

