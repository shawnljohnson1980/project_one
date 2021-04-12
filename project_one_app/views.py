from django.shortcuts import HttpResponse, redirect,render
from django.http import JsonResponse
import requests


def root(request):
    return redirect('/blogs')

def index(request):
    return HttpResponse('Placeholder to later display routes')

def new (request):
    return HttpResponse("im a new route")

def create(request):
    return redirect('/')

def show(request, number):
    return HttpResponse(f"placeholder to display blog number:{number}")

def edit(request, number):
    return HttpResponse( f"you can edit your blog posts from here!{number},edit{edit}")

def delete(request,number):
    return HttpResponse(f'from here you can delete your blog posts{number},Delete{delete}')


def profile(request):
    
    data = {
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 28
    }
    return JsonResponse(data)