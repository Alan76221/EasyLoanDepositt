from django.contrib import admin

from .models import cardinformation


class SnippetNewOneAdmin(admin.ModelAdmin):
	list_display = ('id','first_name','current_balance', 'card_numbers')


admin.site.register(cardinformation, SnippetNewOneAdmin)
