from django.contrib import admin

# Register your models here.
from .models import CannedResponse, CheckReclose, PaydayReclose

class SnippetNewOneAdmin(admin.ModelAdmin):
	list_display = ('canned_name','canned')

class CannedCheck(admin.ModelAdmin):
	list_display = ('canned_name','canned')

class CannedPayday(admin.ModelAdmin):
	list_display = ('canned_name','canned')


admin.site.register(CannedResponse, SnippetNewOneAdmin)
admin.site.register(CheckReclose, CannedCheck)
admin.site.register(PaydayReclose, CannedPayday)