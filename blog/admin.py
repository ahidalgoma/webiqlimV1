from django.contrib import admin
from .models import Categoria, Post
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class PostAdmin(SummernoteModelAdmin): 
    summernote_fields = '__all__'


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)