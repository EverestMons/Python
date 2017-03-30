from django.conf.urls import url, include
from views import *

urlpatterns = [
    url(r'^$', home, name='home' ),
    url(r'^addquote$', addquote, name='addquote' ),
    url(r'^register$', register, name='register'),
]
