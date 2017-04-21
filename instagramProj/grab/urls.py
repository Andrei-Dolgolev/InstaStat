from django.conf.urls import url

from .views import graph , PyData

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^$', graph),
    #url(r'^api/play_count_by_month', play_count_by_month, name='play_count_by_month')
    url(r'^PyData', PyData, name='PyData')
]