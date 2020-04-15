from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination


def index(request):

    destinations = Destination.objects.all()

    return render(request, 'index.html', {'destinations': destinations})
