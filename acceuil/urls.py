from django.conf.urls import url
from acceuil import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]