from django.shortcuts import render

# Create your views here.

def about(request):
  if request.method == 'POST':
    name = request.POST.get('username')
    email = request.POST.get('email')
    select = request.POST.get('select')
  return render(request, 'htmlform/about.html', {'name': name, 'email': email, 'select': select})

def create_form(request):
  if request.method == 'POST':
    name = request.POST.get('username')
    email = request.POST.get('email')
    select = request.POST.get('select')
    print(name, email, select)
  return render(request, 'htmlform/form.html')