from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^contacts/$', views.contact_list, name='contact_list'),
    url(r'^contacts/(?P<contact_id>[0-9]+)$', views.contact_details,
        name='contact_details'),
]
