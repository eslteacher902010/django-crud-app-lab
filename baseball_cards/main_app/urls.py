from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('cards/', views.card_index, name='card-index'),
    path('cards/<int:card_id>/', views.card_detail, name='card-detail'),
    path('cards/create/', views.CardCreate.as_view(), name='card-create'),
    path('cards/<int:pk>/update/', views.CardUpdate.as_view(), name='card-update'),
    path('cards/<int:pk>/delete/', views.CardDelete.as_view(), name='card-delete'),

    path('stats/index/', views.StatList.as_view(), name='stat-index'),
    path('stats/create/', views.StatCreate.as_view(), name='stat-create'),#stat create
    path('stats/<int:pk>/', views.StatDetail.as_view(), name='stat-detail'), #stat detail

    path('stats/<int:pk>/update/', views.StatUpdate.as_view(), name='stat-update'),#stat update
    path('stats/<int:pk>/delete/', views.StatDelete.as_view(), name='stat-delete'),#stat delete
    path('cards/<int:card_id>/add-stat/', views.add_stat, name='add-stat'),

    path('sales/create/', views.SaleCreate.as_view(), name='sale-create'),
    path('cards/<int:card_id>/add-sale/', views.add_sale, name='add-sale'), #add new sales 

    path('sales/<int:pk>/', views.SaleDetail.as_view(), name='sale-detail'),
    path('sales/', views.SaleList.as_view(), name='sale-index'),
    path('sales/<int:pk>/update/', views.SaleUpdate.as_view(), name='sale-update'),
    path('sales/<int:pk>/delete/', views.SaleDelete.as_view(), name='sale-delete'),

    path('accounts/signup/', views.signup, name='signup'),




]

 
 