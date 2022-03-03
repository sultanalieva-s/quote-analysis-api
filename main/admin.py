from django.contrib import admin

# Register your models here.
from main.models import Quote, QuoteAnalysis

admin.site.register(Quote)
admin.site.register(QuoteAnalysis)

