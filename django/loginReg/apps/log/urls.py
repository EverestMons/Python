from django.conf.urls import url
from views import *
urlpatterns = [
    url(r'^$', index),
    url(r'^registerAction$', registerAction, name = 'registerAction'),
    url(r'^success$', success),
    url(r'^login$', loginuser),

]
