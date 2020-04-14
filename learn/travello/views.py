from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination


def index(request):

    dest1 = Destination()
    dest1.name = "Nairobi"
    dest1.desc = "The city that never sleeps"
    dest1.price = 500
    dest1.img = 'destination_1.jpg'

    dest2 = Destination()
    dest2.name = "Kampala"
    dest2.desc = "The city of Museveni"
    dest2.price = 400
    dest2.img = 'destination_2.jpg'

    dest3 = Destination()
    dest3.name = "Dodoma"
    dest3.desc = "The city that keeps singing"
    dest3.price = 600
    dest3.img = 'destination_3.jpg'

    destinations = [dest1, dest2, dest3]
    return render(request, 'index.html', {'destinations': destinations})
