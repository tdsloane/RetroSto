from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def collection(request):
    return render(request, 'catolog/collection.html', {'title':'Collection'})

def search(request):
    return render(request, 'catolog/search.html', {'title': 'Search'})