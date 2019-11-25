from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^schedule/(?P<capital>[0-9]+)/(?P<installments>[0-9]+)/(?P<installment_interval>[0-9]+)/(?P<rate>\d+\.\d+)/(?P<initiation_date>[0-9]{4}-0?[1-12]-0?[1-31])/(?P<method>\w{1})/$', views.schedule, name='schedule'),
]