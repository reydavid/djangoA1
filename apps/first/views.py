from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h3>First Name: David</h3><h3>Last: Sartin</h3><h3>Favorite Movie: Django Unchained</h3><h3>Favorite Music Genre: Trap (for now)</h3>")
