from django.shortcuts import render
from django.http import HttpResponse

def post_list(request):
    return render(request, 'appProg/post_list.html')

def sobre(request):
    return render(request, 'appProg/sobre.html')

def contato(request):
    return render(request, 'appProg/contato.html')