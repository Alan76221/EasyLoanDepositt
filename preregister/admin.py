from django.contrib import admin
from .models import preregisterform


class AdminClass(admin.ModelAdmin):
	list_display = ('id','first_name','loan_amount', 'bank_name', 'current_balance_in_account')


admin.site.register(preregisterform, AdminClass)
