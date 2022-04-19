import json

from django.shortcuts import render


def index(request):
    with open('/programame/src/core/mock.json') as file:
        projects = json.load(file)

    return render(request, 'index.html', {'projects': projects})
