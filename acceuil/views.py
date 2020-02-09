from django.shortcuts import render
from . import forms

# Create your views here.

def index(request):
    form = forms.UserModel()

    if request.method == 'POST':
        form = forms.UserModel(request.POST)

        if form.is_valid():
            form.save(commit=True)
            form = forms.User()
        else:
            print("Formulaire non valide")
    else:
        form = forms.UserModel()

    return render(request, 'acceuil/index.html', {'form': form})

