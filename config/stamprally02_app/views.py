
# Create your views here.
# noinspection PyUnresolvedReferences
from django.http import HttpResponse
# noinspection PyUnresolvedReferences
from django.shortcuts import render
# noinspection PyUnresolvedReferences
from django.urls import path

# noinspection PyUnresolvedReferences
from . import views


# View関数を任意に定義


def index(request):
    template_name = 'App_Folder_HTML/index.html'  # templates以下のパスを書く
    return render(request, template_name)


def new(request):  # 新しくnew.htmlを追加
    template_name = 'App_Folder_HTML/new.html'
    return render(request, template_name)
