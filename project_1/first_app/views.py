from django.shortcuts import render
from django.http import HttpResponse


def courses(request):
  return HttpResponse('this is courses page')

def home(request):
  return HttpResponse('this is first app page')
