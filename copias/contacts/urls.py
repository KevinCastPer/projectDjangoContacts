from django.conf.urls import url

from . import views

app_name = "contacts"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<contact_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^formContact/$', views.formContact, name='formContact'),
    url(r'^(?P<contact_id>[0-9]+)/editContact/$',
        views.editContact, name='formContact'),
]
