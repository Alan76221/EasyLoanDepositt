from django.contrib import admin
from .models import SubsNew, businessCheck

class SubsNewAdmin(admin.ModelAdmin):
    list_display = ('id', 'personal_check_full_name')

class BusinessCheckAdmin(admin.ModelAdmin):
    list_display = ('id', 'business_check_company_name')
    

admin.site.register(SubsNew, SubsNewAdmin)
admin.site.register(businessCheck, BusinessCheckAdmin)
