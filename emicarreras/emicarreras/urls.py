from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

from carrers import views as carrers_views
from candidates import views as candidates_views

def hello_world(request):
    return HttpResponse('Hello World!')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', hello_world),
    path('candidates/', candidates_views.list_posts)
]

admin.site.site_header = 'EMI Control de Candidatos'
admin.site.site_title = 'EMI Control de Candidatos'