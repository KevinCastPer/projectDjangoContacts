from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^contacts/$', views.ContactList.as_view(), name='contact_list'),
    url(r'^contacts/(?P<contact_id>[0-9]+)$', views.ContactDetails.as_view(),
        name='contact_details'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
