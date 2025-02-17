from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.generic import View

from authentication.models import User
from forms.forms import InscriptionForm, LoginForm


def logout_user(request):
    logout(request)
    return redirect('login')

class InscriptionPage(View):
    inscription_form = InscriptionForm
    inscription_page_url = 'authentication/inscription.html'
    
    def get(self, request):
        form = self.inscription_form()
        return render(request, self.inscription_page_url, {'form': form})
    
    def post(self, request):
        form = self.inscription_form(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        return render(request, self.inscription_page_url, {'form': form})

class LoginPage(View):
    form_class = LoginForm
    render_url = message = 'authentication/login.html'

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.render_url, {"form": form, "message": message})

    def post(self, request):
        form = self.form_class()
        message = ''
        if request.method == 'POST':
            form = self.form_class(request.POST)

            if form.is_valid():
                user = authenticate(
                    username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                
                if user is not None:
                    login(request, user)
                    return redirect('home')
                
            message = "Erreur est survenue lors de la connexion"
        return render(request, 'authentication/login.html', {"form": form, "message": message})


