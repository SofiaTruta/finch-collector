from django.shortcuts import render
from .models import Finch


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def all_finches(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html',{
        'finches': finches
    })

def single_finch(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/single-finch.html', {
        'finch': finch
    })