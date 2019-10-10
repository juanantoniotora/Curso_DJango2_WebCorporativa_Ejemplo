from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'piblished','post_categories')
    ordering = ('author', 'piblished')
    search_fields = ('title', 'cotent','author__username', 'categories__name')
    date_hierarchy = 'piblished'
    list_filter = ('categories__name', 'author__username')

    ## defino nuestros propios metodos
    def post_categories(self, obj): #este obj es el objeto que ejecuta cada fila de la tabla
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    ## definimos un nombre agradable a la nueva columna "categorias"
    post_categories.short_description = "categorias"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)