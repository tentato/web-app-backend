from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def main(request):
  template = loader.get_template('main_template.html')
  return HttpResponse(template.render())