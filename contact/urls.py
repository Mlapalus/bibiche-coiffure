from django.conf.urls import url
from contact import views

urlpatterns = [
    url(r'^$', views.formContactView, name='contact'),
]