from django.contrib import admin
from .models import Snippet

@admin.register(Snippet)
class SnippetSdmin(admin.ModelAdmin):
    pass
