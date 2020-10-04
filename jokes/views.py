#from django.shortcuts import render
from django.views.generic import ListView
from .models import Joke

# Minimal list view
class JokeListView(ListView):
    model = Joke



