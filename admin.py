from django.contrib import admin
from .models import FacLogin,Document,Faculty
# Register your models here.
admin.site.register(FacLogin)
admin.site.register(Document)
admin.site.register(Faculty)