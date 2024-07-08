from django.shortcuts import render
from django.views import View

class PageHome(View):
    def get(self, request):
        return render(request, 'appHome/home/index.html')