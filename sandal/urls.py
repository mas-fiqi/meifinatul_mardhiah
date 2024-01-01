from django.contrib import admin
from django.urls import include, path
from ayo.views import *

urlpatterns = [
    path('', vina, name='vina'),
    # path('hom', hom, name='hom'),
    # path('comen', comen, name='comen'),
    # path('contact', contact, name='contact'),
    path('admin/', admin.site.urls),
]