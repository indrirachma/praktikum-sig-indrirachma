from django.urls import path
from . import view_gempa

urlpatterns = [
    path('', view_gempa.gempaterkini, name='gempaterkini'),
]