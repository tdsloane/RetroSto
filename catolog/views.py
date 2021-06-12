from django.views.generic.detail import DetailView
from catolog.models import Game, UserQuery
from django.shortcuts import render
from django.views.generic import ListView
from catolog.game_getter import search_query
from .models import UserSearch

# Create your views here.
def collection(request):
    context = {
        'games': Game.objects.all()
    }
    return render(request, 'catolog/collection.html', context)


exp_time = False
def search(request):
    q = request.POST.get('q')
    user_input=''
    form = UserSearch(request.POST or None)
    if form.is_valid():
        user_input = form.cleaned_data.get('user_input')
    context = {'form': form, 'user_input': user_input, 'q': q}
    search_query(user_input, exp_time)



class GameListView(ListView):
    model = Game
    template_name = 'catolog/collection.html'
    context_object_name = 'games'

class GameDetailView(DetailView):
    model = Game

