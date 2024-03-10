from django.shortcuts import render, HttpResponse

# Create your views here.

def hello_world(request, nome, idade):
    return HttpResponse('<h1>Oi, {} você ja tem {} anos!</h1>'.format(nome, idade))
