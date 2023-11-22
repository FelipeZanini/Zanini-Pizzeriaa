from django.shortcuts import render, redirect
from django.contrib import messages


def home(request):
    return render(request, 'index.html')


def menu(request):
    return render(request, 'menu.html')


def menu_items(request):
    return render(request, 'menu_items.html')