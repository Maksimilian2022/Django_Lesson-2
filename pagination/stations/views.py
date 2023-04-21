from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

def index(request):
    return redirect(reverse('bus_stations'))


def CONTENT():
    with open('data-398-2018-08-30.csv', 'r', encoding='utf8') as csv_content:
        reader = csv.DictReader(csv_content)
        CONTENT = [content for content in reader]
    return CONTENT


def bus_stations(request):
    page = request.GET.get('page', 1)
    content = CONTENT()
    paginator = Paginator(content, 10)
    request_page = paginator.get_page(page)

    context = {
        'bus_stations': request_page,
        'page': request_page,
    }
    return render(request, 'stations/index.html', context)
