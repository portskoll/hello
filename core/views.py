from django.shortcuts import render, HttpResponse

# Create your views here.

def hello_world(request, nome, idade):
    return HttpResponse('<h1>Oi, {} você ja tem {} anos!</h1>'.format(nome, idade))


def hello_soma(request, n1, n2):
    op = n1 + n2
    return HttpResponse('<h1>O resultado da soma de {} e {} = {} </h1>'.format(n1, n2, op))


def hello_multiplicacao(request, n1, n2):
    op = n1 * n2
    return HttpResponse('<h1>O resultado da multiplicação de {} e {} = {} </h1>'.format(n1, n2, op))


def hello_subtracao(request, n1, n2):
    op = n1 - n2
    return HttpResponse('<h1>O resultado da subtração de {} e {} = {} </h1>'.format(n1, n2, op))


def hello_divisao(request, n1, n2):
    op = n1 / n2
    return HttpResponse('<h1>O resultado da divisão de {} e {} = {} </h1>'.format(n1, n2, op))
