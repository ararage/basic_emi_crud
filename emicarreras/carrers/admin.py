from django.contrib import admin
from carrers.models import Carrer


class CarrersAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'places_h',
        'places_m'
    ]
    list_display_links = None
    list_editable = ('name','places_h','places_m',)
    list_filter = ['name']
    search_fields = ['name']

admin.site.register(Carrer, CarrersAdmin)
