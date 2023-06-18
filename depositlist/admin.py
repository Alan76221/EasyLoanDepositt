from django.contrib import admin
from depositlist.models import Deposit_List, Received_List
class SnippetNewOneAdmin(admin.ModelAdmin):
	list_display = ('full_name',)

class CannedCheck(admin.ModelAdmin):
	list_display = ('full_name',)


admin.site.register(Deposit_List, SnippetNewOneAdmin)
admin.site.register(Received_List, CannedCheck)