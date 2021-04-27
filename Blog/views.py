from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1> WOW ! Started executing small modules in a sequential manner </h1>")