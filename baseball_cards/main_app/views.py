from django.shortcuts import redirect, render, get_object_or_404
#the view in django is the controller in MVC
# Create your views here.

from .models import Card, Stat, Sale

from django.views.generic.edit import CreateView
from .forms import StatForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView #import generic class-based views

from django.contrib.auth.views import LoginView


class Home(LoginView):
    template_name = 'home.html'


def about(request):
    return render(request, 'about.html')

def card_index(request):
    cards = Card.objects.all()
    return render(request, 'cards/index.html', {'cards': cards})

def card_detail(request, card_id):
    card = Card.objects.get(id=card_id)
    stat_form = StatForm()
    return render(request, 'cards/detail.html', {'card': card, 'stat_form': stat_form})

class CardCreate(CreateView):
    model = Card
    fields = '__all__'

    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
        # Let the CreateView do its job as usual 
        return super().form_valid(form) #esssentialy slows down the process to assign user

class CardUpdate(UpdateView):
    model = Card
    fields = ['brand', 'year', 'description', 'condition', 'price', 'image_filename']

class CardDelete(DeleteView):
    model = Card
    success_url = '/cards/'


class StatCreate(CreateView):
    model = Stat
    fields ='__all__'

class StatList(ListView):
    model = Stat

class StatDetail(DetailView):
    model = Stat

class StatUpdate(UpdateView):
    model = Stat
    fields = ['date', 'stat']

class StatDelete(DeleteView):
    model = Stat
    success_url = '/stats/' 

def associate_stat(request, card_id, stat_id):
    # Note that you can pass a stat's id instead of the whole object
    Card.objects.get(id=card_id).stats.add(stat_id)
    return redirect('card-detail', card_id=card_id)


def add_stat(request, card_id):
    # create a ModelForm instance using the data in request.POST
    form = StatForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the card_id assigned
        new_stat = form.save(commit=False) #don't save it right away
        new_stat.card_id = card_id
        new_stat.save()
    return redirect('card-detail', card_id=card_id)

class SaleCreate(CreateView):
    model = Sale
    fields = '__all__'


class SaleList(ListView):
    model = Sale

class SaleDetail(DetailView):
    model = Sale

class SaleUpdate(UpdateView):
    model = Sale
    fields = ['date', 'amount', 'card']

class SaleDelete(DeleteView):
    model = Sale
    success_url = '/sales/'