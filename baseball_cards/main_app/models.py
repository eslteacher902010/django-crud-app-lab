from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



class Sale(models.Model):
    date = models.DateField('sale date')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    card = models.ForeignKey('Card', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.card.name} sold on {self.date} for ${self.amount}"

    def get_absolute_url(self):
        return reverse('sale-detail', kwargs={'pk': self.id})



STATS = (
    ('RBI', 'runs batted in'),
    ('W', 'Wins'),
    ('HR', 'Home Runs'),
    ('H', 'Hits')
)

class Card(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()
    condition = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_filename = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('card-detail', kwargs={'card_id': self.id})

class Stat(models.Model): # new model
    date = models.DateField('Stat updated on:')
    stat = models.CharField(  # better name than "meal"
        max_length=3,  # longest code is 3 chars: 'RBI'
        choices=STATS,
        default=STATS[0][0]
    )
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_stat_display()} on {self.date}"

class Meta: 
        ordering = ['-date'] # most recent first
