from django.conf.urls import url
from views import *
urlpatterns = [
    url(r'^$', index, name = 'index'),
    url(r'^login$', loginFormAction, name = 'login'),
    url(r'^addbook$', addBook, name = 'addbook'),
    url(r'^library$', library, name = 'library'),
    url(r'^bookPage$', bookPage, name = 'bookPage'),
    url(r'^bookProfile/(?P<id>\d+)$', bookProfile, name = 'bookProfile'),
    url(r'^registerFormAction$', registerFormAction, name = 'register'),
    url(r'^displayUser/(?P<id>\d+)$', displayUser, name = 'displayUser'),

]
