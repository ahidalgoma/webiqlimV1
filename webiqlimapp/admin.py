from django.contrib import admin

# Register your models here.
from .models import ParamWeb
from django_summernote.admin import SummernoteModelAdmin

# Apply summernote to all TextField in model.
class ParamWebAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(ParamWeb, ParamWebAdmin)
