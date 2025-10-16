from django.contrib import admin

# Register your models here.
from .models import Card, Stat, Sale
# Register your models here.
admin.site.register(Card)
admin.site.register(Stat)
admin.site.register(Sale)