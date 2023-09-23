from django.shortcuts import render
from .models import Ability

def home(request):
    abilitys = Ability.objects.all()
    return render(request, 'abilitys/home.html', {'abilitys': abilitys})



