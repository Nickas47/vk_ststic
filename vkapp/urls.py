from django.conf.urls import url
from . import views

app_name = "vkapp"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^vkapp/$', views.result, name='result'),
]
