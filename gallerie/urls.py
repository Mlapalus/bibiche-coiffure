from django.conf.urls import url
from gallerie import views

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    url(r'^$', views.gallerie, name='gallerie'),
]

urlpatterns += staticfiles_urlpatterns()
