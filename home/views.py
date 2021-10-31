from django.shortcuts import render
from django.views import generic

from .models import Word


def index(request):
    words = Word.get_words(5)
    context = {'words': words}
    return render(request, 'home/index.html', context=context)


class WordView(generic.ListView):
    model = Word
    template_name = "home/index.html"
