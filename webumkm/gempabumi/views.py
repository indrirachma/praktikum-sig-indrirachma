from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return HttpResponse("<h1>Selamat datang di Peta Gempa Bumi</h1>")