from django.shortcuts import render
from django.core.mail import send_mail
from . import forms
# Create your views here.


def contact(request):
    return render(request, 'contact/contact.html', context=None)


def formContactView(request):
    form = forms.FormContact()

    if request.method == 'POST':
        form = forms.FormContact(request.POST)

        if form.is_valid():
            # DO SOMETHING CODE
            send_mail(form.cleaned_data['sujet'],
                        form.cleaned_data['message'],
                        form.cleaned_data['email'],
                        ['mimibato@gmail.com'],
                        fail_silently=False,
                        )
        else:
            print("Non Valide")
    else:
        form = forms.FormContact()

    return render(request,'contact/contact.html',{'form':form})
