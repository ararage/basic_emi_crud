from django.contrib import admin
from candidates.models import Candidate, Carrer
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db import transaction, DatabaseError
from import_export.admin import ImportExportModelAdmin
from candidates.resources import CandidateResource

class CandidatesAdmin(ImportExportModelAdmin):
    resource_class = CandidateResource
    list_display = [
        'id',
        'first_name', 
        'last_name',
        'matriname',
        'get_carrer',
        'get_gender'
    ]
    # list_editable = ['first_name', 'last_name',]
    list_filter = [
        'first_name',
        'last_name',
        'matriname',
        'carrer__name',
        'gender__name'
    ]
    # search_fields = ['first_name', 'last_name']
    list_display_links = [
        'first_name'
    ]

    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': 'Gestión de Canidatos'}
        return super(CandidatesAdmin, self).changelist_view(request, extra_context=extra_context)

    def get_carrer(self, obj: Candidate):
        return obj.carrer.name if obj.carrer else ''

    def get_gender(self, obj: Candidate):
        return obj.gender.name if obj.gender else ''

    def save_model(self, request, obj, form, change):
        try:
            with transaction.atomic():
                if obj.gender.name == 'Hombre' and obj.carrer.places_h > 0 or obj.gender.name == 'Mujer' and obj.carrer.places_m > 0:
                    obj.save()
                    # Restamos lugares por género
                    if obj.gender.name == 'Hombre':
                        obj.carrer.places_h = obj.carrer.places_h - 1
                        obj.carrer.save() 
                        d = obj.carrer.places_h
                    else:
                        obj.carrer.places_m = obj.carrer.places_m - 1
                        obj.carrer.save() 
                        d = obj.carrer.places_m

                    messages.set_level(request, messages.WARNING)
                    g = obj.gender.name
                    c_c = Carrer.objects.filter(name=obj.carrer.name).count()
                    c = c_c + d
                    a = obj.carrer.name
                    messages.warning(request, 'Arma : {} - Lugares disponibles {} - Género {} - Cuota: {}'.format(a, d, g, c))
                else:
                    messages.set_level(request, messages.ERROR)
                    messages.error(request, 'No hay cuota disponible para {}'.format(obj.carrer.name))
                    return HttpResponseRedirect(request.path)
        except DatabaseError as e:
            # logger.exception("Naming update transaction DB error")
            messages.error(request, 'Error en la transacción {}'.format(e))
            return HttpResponseRedirect(request.path)

    get_carrer.admin_order_field = 'carrer__name'
    get_carrer.short_description = 'Arma'
    get_carrer.admin_list_filter = 'carrer__name'

    get_gender.admin_order_field = 'gender__name'
    get_gender.short_description = 'Género'
    get_gender.admin_list_filter = 'gender__name'

admin.site.register(Candidate, CandidatesAdmin)
