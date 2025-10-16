from decimal import Decimal
from django.shortcuts import redirect, render, get_object_or_404
#the view in django is the controller in MVC
# Create your views here.
from datetime import date


from .models import Card, Stat, Sale

from django.views.generic.edit import CreateView
from .forms import StatForm, SaleForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView #generic class views

from django.contrib.auth.views import LoginView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Import the login_required decorator
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin


class Home(LoginView):
    template_name = 'home.html'


def about(request):
    return render(request, 'about.html')

@login_required
def card_index(request):
    cards = request.user.card_set.all()
    return render(request, 'cards/index.html', {'cards': cards})

def card_detail(request, card_id):
    card = Card.objects.get(id=card_id)
    stat_form = StatForm()
    sale_form = SaleForm()
    return render(request, 'cards/detail.html', {'card': card, 'stat_form': stat_form})

class CardCreate(LoginRequiredMixin,CreateView):
    model = Card
    fields = '__all__'

    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the card
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

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect('card-index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
    # Same as: 
    # return render(
    #     request, 
    #     'signup.html',
    #     {'form': form, 'error_message': error_message}
    # )

def add_sale(request, card_id):
    card = get_object_or_404(Card, id=card_id)

    # Example default: today’s date and a placeholder amount
    Sale.objects.create(
        card=card,
        date=date.today(),
        amount=Decimal("20.00")  # You can later replace with form data
    )

    return redirect('card-detail', card_id=card_id)