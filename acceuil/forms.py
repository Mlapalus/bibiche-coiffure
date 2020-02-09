from django import forms
from .models import User


class UserModel(forms.ModelForm):
    class Meta():
        model = User
        fields = ['nom', 'email']
        widgets = {
                    'nom' : forms.TextInput(attrs={'class': "form-control",'placeholder':"Votre Nom"}),
                    'email' : forms.TextInput(attrs={'class': "form-control",'placeholder':"Votre email"}),
                    }
