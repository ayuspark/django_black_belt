from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.to_login, name='to_login'),
    url(r'^register$', views.to_register, name='to_register'),
    url(r'^logout$', views.to_logout, name='to_logout'),
]
