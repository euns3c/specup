from django.shortcuts import render
from django.db.models import Sum
from .models import UserPointHistory

# Create your views here.

def specup(request):
    lists = UserPointHistory.objects.all().order_by('user')
    points = UserPointHistory.objects.all().aggregate(Sum('delta'))
    return render(request, 'specup/list.html', {'lists': lists})
