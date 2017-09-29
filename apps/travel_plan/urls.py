from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^join/(?P<plan_id>\d+)$', views.join, name='join'),
    url(r'^add$', views.add, name='add'),
    url(r'^destination/(?P<plan_id>\d+)$', views.plan_destination, name='plan_destination'),
]
