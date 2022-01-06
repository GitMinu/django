from django.urls import path

from .views import *

urlpatterns = [
    path('', home_page, name='home_page'),
    path('entry/', parking_entry, name='parking entry'),
    path ('exit/',parking_exit, name='parking exit')
]