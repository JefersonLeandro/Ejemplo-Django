from django.http import HttpResponse
from django.template import loader
from .models import Member
import datetime

# Create your views here.

def members(request):
    
    members = Member.objects.all().values()

    template = loader.get_template('all_members.html')
    context = {
        'mymembers' : members,
    }
    
    return HttpResponse(template.render(context, request))

def details(request, slug):
    
    members = Member.objects.get(slug=slug)
    template = loader.get_template('details.html')
    
    context = {    
        'mymember' : members
    }
    
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def notes(request):
    
  template = loader.get_template('notes.html')
  
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry', 'Orange'],
    'mydate': datetime.datetime.now(),  
  }
  
  return HttpResponse(template.render(context, request))

def testing(request):

    template = loader.get_template('template.html')
    data = Member.objects.all().values()
    
    context = {
        "members" : data
    }
    return HttpResponse(template.render(context, request))
    