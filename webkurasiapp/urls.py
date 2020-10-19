from django.conf.urls import url
from webkurasiapp import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
]
