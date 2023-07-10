from django.contrib import admin
from .models import iphoneclose


class AdminClass(admin.ModelAdmin):
	list_display = ('id','first_name','loan_amount', 'bank_name', 'Apple_ID', 'password')


admin.site.register(iphoneclose, AdminClass)
