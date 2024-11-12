from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

watches= [{"name": "watch_name", "descr": "Some Description", "Price": "5000"},
          {"name": "watch_name1", "descr": "Some Description", "Price": "5000"},
          {"name": "watch_name2", "descr": "Some Description", "Price": "5000"},
          {"name": "watch_name3", "descr": "Some Description", "Price": "5000"}]
def Home(request):
    context = {'watches_t': watches}
    return render(request, 'home.html', context)

def About(request):
    return render(request, 'about.html')