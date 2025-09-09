from django.shortcuts import render
from .forms import createForm

# Create your views here.

def home(request):
  if request.method == 'POST':
    form = createForm(request.POST)
    if form.is_valid():
      print(form.cleaned_data)
  else:
    form = createForm()
  return render(request, 'home.html', {'form': form})