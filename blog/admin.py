from django.contrib import admin
from .models import Categoria, Post
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class PostAdmin(SummernoteModelAdmin): 
    summernote_fields = '__all__'
    list_display=('titulo', 'autor', 'created')
    list_filter=('categorias', 'created')
    date_hierarchy='created'
    search_fields=('titulo', '6contenido')
    


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)