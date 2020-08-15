from import_export import resources
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget, Widget

from candidates.models import Candidate


class CandidateResource(resources.ModelResource):
    id = Field(attribute='id', column_name='ID')
    first_name = Field(attribute='first_name', column_name='NOMBRES')
    last_name = Field(attribute='last_name', column_name='APELLIDO P.')
    matriname = Field(attribute='matriname', column_name='APELLIDO M.')
    carrer = Field(attribute='carrer__name', column_name='ARMA')
    gender = Field(attribute='gender__name', column_name='GENERO')

    class Meta:
        model = Candidate
        export_order = (
            'id',
            'first_name',
            'last_name',
            'matriname',
            'carrer',
            'gender',
        )