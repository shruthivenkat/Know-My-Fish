from django.shortcuts import render
from skeleton.models import Restaurant

# Create your views here.
from django.http import HttpResponse

def index(request):
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants': restaurants
    }
    return render(request, 'project_index.html', context)