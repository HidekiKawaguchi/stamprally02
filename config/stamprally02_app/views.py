# noinspection PyUnresolvedReferences
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
    # 変数設定
    params = {"message_me": "Hello World"}
    # 出力
    return render(request, 'App_Folder_HTML/index.html', context=params)
