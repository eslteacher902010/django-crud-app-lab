from django.shortcuts import render

# Create your views here.
# Define the home view function
def home(request): #this home is different from the home in urls.py because this is a function
    # Send a simple HTML response
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class Card:
    def __init__(self, name, brand, description, year, condition, price, image_filename):
        self.name = name
        self.brand = brand
        self.description = description
        self.year = year
        self.condition = condition
        self.price = price
        self.image_filename = image_filename  # New attribute for image filename    
    

cards = [
        Card("Babe Ruth", "Topps", "Legendary baseball player", 1933, "Mint", 1000000, "babe.jpg"),
        Card("Mickey Mantle", "Topps", "Famous New York Yankees player", 1952, "Near Mint", 500000, "mickey_mantle.jpg"),
        Card("Willie Mays", "Topps", "One of the greatest all-around players", 1951, "Excellent", 300000,"mays.jpg"),
        Card("Ted Williams", "Topps", "Legendary Boston Red Sox player", 1951, "Excellent", 300000, "ted.jpg"),
    ]

def card_index(request):
    
    return render(request, 'cards/index.html', { 'cards': cards }) 