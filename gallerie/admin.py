from django.contrib import admin
from django.utils.text import Truncator
from gallerie.models import MyPhotoModel

# Register your models here.

class MyPhotoModelAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_creation')
    list_filter = ('titre', 'date_creation')
    date_hierarchy = 'date_creation'
    ordering = ('date_creation',)
    search_fields = ('titre', 'date_creation')
    empty_value_display = '-empty-'


    # Configuration du formulaire d'édition
    fieldsets = (
        # meta-info (titre, auteur)
        ('Général', {
            'classes' : ['collapse',],
            'fields' : ('titre','date_creation','image'),
        }),
    
    )

admin.site.register(MyPhotoModel, MyPhotoModelAdmin)

