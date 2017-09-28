from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^books/(?P<book_id>\d+)$', views.book_detail, name='book_detail'),
    url(r'^books/(?P<book_id>\d+)/add_review$', views.book_add_review, name='book_add_review'),
    url(r'^books/add$', views.add_book, name='add_book'),
    url(r'^books/(?P<book_id>\d+)/review/(?P<review_id>\d+)/delete$',
        views.review_delete, name='review_delete'),
    url(r'^users/(?P<user_id>\d+)$', views.user_detail, name='user_detail'),
]
