from django.contrib import admin
from .models import Vulnerability, ValidatedResult
# Register your models here.

admin.site.register(Vulnerability)
admin.site.register(ValidatedResult)