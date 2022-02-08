# noinspection PyUnresolvedReferences
# Create your views here.
# noinspection PyUnresolvedReferences
from django.http import HttpResponse
from django.shortcuts import render


# View関数を任意に定義
def index(request):
    return HttpResponse("Hello World")
