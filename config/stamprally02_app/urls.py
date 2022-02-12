# noinspection PyUnresolvedReferences
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),  # 追記
]
