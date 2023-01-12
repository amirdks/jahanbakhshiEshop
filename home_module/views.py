from django.shortcuts import render
from django.utils.text import slugify
from django.views.generic import TemplateView


# Create your views here.

class HomeView(TemplateView):
    template_name = 'home_module/home_page.html'

    # def get_context_data(self, **kwargs):
    #     name = 'امیر حسین'
    #     print(slugify(name, allow_unicode=True), '----', name)
    #     return super(HomeView, self).get_context_data(**kwargs)
