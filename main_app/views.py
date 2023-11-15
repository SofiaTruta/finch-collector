from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from .models import Finch, Snack
from .forms import FeedingForm


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
    feeding_form = FeedingForm()
    # connect the snacks
    snacks_list = finch.snacks.all().values_list('id') # a list of the snacks finch has tried
    snacks_finch_hasnot_tried = Snack.objects.exclude(id__in=snacks_list)# list of snacks not on the previous list
    return render(request, 'finches/single-finch.html', {
        'finch': finch,
        'feeding_form': feeding_form,
        'snacks': snacks_finch_hasnot_tried
    })

def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('single_finch', finch_id=finch_id)
    
def connect_snack(request, finch_id, snack_id):
    Finch.objects.get(id=finch_id).snacks.add(snack_id)
    return redirect('single_finch', finch_id=finch_id)

def remove_snack(request, finch_id, snack_id):
    Finch.objects.get(id=finch_id).snacks.remove(snack_id)
    return redirect('single_finch', finch_id=finch_id)

# CRUD for Finch
class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'species', 'description', 'where_to_find']

class FinchUpdate(UpdateView):
    model = Finch
    fields = '__all__'

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'


#  CRUD for Snack
class SnackList(ListView):
    model = Snack

class SnackDetail(DetailView):
    model = Snack

class SnackCreate(CreateView):
    model = Snack
    fields = '__all__'
    success_url = '/snacks'

class SnackUpdate(UpdateView):
    model = Snack
    fields = '__all__'

class SnackDelete(DeleteView):
    model = Snack
    success_url = '/snacks'