from django.conf.urls import url

from . import views

app_name = 'app'
urlpatterns = [
    url(r'^index/', views.index),
    url(r'^health', views.health, name='health'),
]
