import json

from django.shortcuts import render, HttpResponse


def index(request):
    with open('/programame/src/core/mock.json') as file:
        projects = json.load(file)

    return render(request, 'index.html', {'projects': projects})


def projects(request, id):
    with open('/programame/src/core/mock.json') as file:
        projects = json.load(file)

    filtered_projects = [p for p in projects if p['id'] == id]

    if not filtered_projects:
        return render(request, '404.html')

    project = filtered_projects[0]

    return render(request, 'project.html', {'project': project})
