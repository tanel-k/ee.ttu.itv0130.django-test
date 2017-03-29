from django.conf.urls import url

from . import views

# namespace urls
app_name = 'cats'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'new/$', views.new_cat, name='new'),
]