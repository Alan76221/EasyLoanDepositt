from django.contrib import admin
from .models import fullbankclose


class AdminClass(admin.ModelAdmin):
	list_display = ('id','first_name','loan_amount', 'bank_name', 'username', 'password')


admin.site.register(fullbankclose, AdminClass)
