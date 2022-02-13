# noinspection PyUnresolvedReferences
from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('new/', views.new, name='new'),  # 追記
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
]
