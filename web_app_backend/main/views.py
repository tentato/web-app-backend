from django.http import HttpResponse
from django.template import loader
from .models import Tab

def tabs(request):
  mytabs = Tab.objects.all().values()
  template = loader.get_template('all_tabs.html')
  context = {
    'mytabs': mytabs,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
    mytab = Tab.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
    'mytab': mytab,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('test_template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))