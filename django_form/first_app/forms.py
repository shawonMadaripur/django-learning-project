from django import forms

class createForm(forms.Form):
  name = forms.CharField()
  email = forms.EmailField()