from django.shortcuts import render
from portfolio.models import *
def index(request):
    projects = Project.objects.all()
    dct = {'title': 'Main page', 'projects': projects}
    return render(request, 'portfolio/index.html', context=dct)
