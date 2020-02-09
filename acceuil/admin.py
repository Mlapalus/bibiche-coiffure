from django.contrib import admin
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('nom','email')
    list_filter = ('nom','email')
    ordering = ('nom',)
    search_fields = ('nom','email')
    empty_value_display = '-empty-'


    # Configuration du formulaire d'édition
    fieldsets = (
        # meta-info (titre, auteur)
        ('Général', {
            'classes' : ['collapse',],
            'fields' : ('nom','email'),
        }),
    
    )

admin.site.register(User, UserAdmin)
