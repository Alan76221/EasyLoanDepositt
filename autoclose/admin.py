from django.contrib import admin
from .models import autoclosesnippet


class SnippetNewOneAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'username', 'password1')


admin.site.register(autoclosesnippet, SnippetNewOneAdmin)
