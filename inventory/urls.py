from django.conf.urls import url
from .views import *

urlpatterns = [

    url(r'^$', index, name='index'),
    url(r'^map', index, name='map'),
    url(r'^display_laptops$', display_laptops, name='display_laptops'),
    url(r'^display_desktops$', display_desktops, name='display_desktops'),
    url(r'^display_mobiles$', display_mobiles, name='display_mobiles'),
    url(r'^display_equipment$', display_equipment, name='display_equipment'),

    url(r'^add_laptop$', add_laptop, name='add_laptop'),
    url(r'^add_desktop$', add_desktop, name='add_desktop'),
    url(r'^add_mobile$', add_mobile, name='add_mobile'),
    url(r'^add_equipment$', add_equipment, name='add_equipment'),

    url(r'^edit_laptop/(?P<pk>\d+)$', edit_laptop, name='edit_laptop'),
    url(r'^edit_desktop/(?P<pk>\d+)$', edit_desktop, name='edit_desktop'),
    url(r'^edit_mobile/(?P<pk>\d+)$', edit_mobile, name='edit_mobile'),
    url(r'^edit_equipment/(?P<pk>\d+)$', edit_equipment, name='edit_equipment'),

    url(r'^delete_laptop/(?P<pk>\d+)$', delete_laptop, name='delete_laptop'),
    url(r'^delete_mobile/(?P<pk>\d+)$', delete_mobile, name='delete_mobile'),
    url(r'^delete_desktop/(?P<pk>\d+)$', delete_desktop, name='delete_desktop'),
    url(r'^delete_equipment/(?P<pk>\d+)$', delete_equipment, name='delete_equipment'),
]
