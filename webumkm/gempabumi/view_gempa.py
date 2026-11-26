from django.shortcuts import render
from django.http import HttpResponse, request

def gempaterkini(request):
    return render (request, 'gempabumi/gempaterkini.html')  