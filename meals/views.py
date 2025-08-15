from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_meal(request):
    return HttpResponse("Welcome to the School Meals Menu Project!")
