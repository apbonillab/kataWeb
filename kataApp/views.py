from django.shortcuts import render

# Create your views here.
from django.template import context


def index(request):
    print('main')
    return render(request, 'kata/index.html')
