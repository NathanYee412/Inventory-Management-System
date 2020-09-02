from django.conf.urls import url
from .views import *

urlpatterns = [

    url(r'^$', index, name='index'),
    url(r'^display_laptops$', display_laptops, name='display_laptops'),
    url(r'^display_desktops$', display_desktops, name='display_desktops'),
    url(r'^display_mobiles$', display_mobiles, name='display_mobiles'),
    url(r'^display_equipment$', display_equipment, name='display_equipment'),

    url(r'^add_laptop$', add_laptop, name='add_laptop'),
    url(r'^add_desktop$', add_desktop, name='add_desktop'),
    url(r'^add_mobile$', add_mobile, name='add_mobile'),
    url(r'^add_equipment$', add_equipment, name='add_equipment'),


]
