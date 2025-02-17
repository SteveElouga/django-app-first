from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

# @login_required
# def home_page(request):
#     return render(request, 'blog/home.html')

class HomePage(LoginRequiredMixin, View):
    home_page_url = 'blog/home.html'
    
    def get(self, request):
        return render(request, self.home_page_url)
