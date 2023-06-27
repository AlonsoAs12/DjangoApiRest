from . import views
from django.urls import re_path as url

urlpatterns = [
    url(r'^libros/$', views.prestamo_list),
    url(r'^libros/(?P<pk>[0-9]+)/$',views.prestamo_detail),
]