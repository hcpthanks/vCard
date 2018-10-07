from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse


def home(request):
    """vCard 首页
    """
    return render(request, 'index.html')
