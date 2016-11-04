from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^algo/(?P<algo_slug>[\w-]+)/$', views.show, name="show_algo")
]