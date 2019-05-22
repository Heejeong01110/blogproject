from django.contrib import admin
from .models import Blog
from portfolio.models import Portfolio
# Register your models here.
admin.site.register(Blog)
admin.site.register(Portfolio)