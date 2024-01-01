from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def vina(request):
  template = loader.get_template('vina.html')
  return HttpResponse(template.render())
# def comen(request):
#   template = loader.get_template('comen.html')
#   return HttpResponse(template.render())

# def work(request):
#   template = loader.get_template('work.html')
#   return HttpResponse(template.render())
# def contact(request):
#   template = loader.get_template('contact.html')
#   return HttpResponse(template.render())

