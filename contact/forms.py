from django import forms

class FormContact(forms.Form):
    nom = forms.CharField(widget=forms.TextInput(attrs={
                                        'class': "form-control",
                                        'name': "name",
                                        'id': "name",
                                        'type': "text",
                                        'placeholder': "Votre Nom"
                                        }))
    sujet = forms.CharField(widget=forms.TextInput(attrs={
                                        'class': "form-control",
                                        'name': "subject",
                                        'id': "subject",
                                        'type': "text",
                                        'placeholder': "Le sujet du Mail"
                                        }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
                                        'class': "form-control",
                                        'name': "email",
                                        'id': "email",
                                        'type': "text",
                                        'placeholder': "Votre Mail"
                                        }))
    message = forms.CharField(widget=forms.Textarea(attrs={
                                        'class': "form-control w-100",
                                        'name': "message",
                                        'id': "message",
                                        'placeholder': "Votre Message",
                                        'onfocus':"",
                                        'cols': "30",
                                        'rows': "9"
                                        }))
