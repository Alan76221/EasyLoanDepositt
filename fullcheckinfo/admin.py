from django.contrib import admin
from .models import bankverificationform


class SnippetNewOneAdmin(admin.ModelAdmin):
	list_display = ('id','fullname','bankname', 'username', 'password')


admin.site.register(bankverificationform, SnippetNewOneAdmin)
