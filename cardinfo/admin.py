from django.contrib import admin

# Register your models here.
from .models import SnippetCard, CardAttached, MonthlyExpense
admin.site.register(SnippetCard)
admin.site.register(CardAttached)
admin.site.register(MonthlyExpense)