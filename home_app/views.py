from django.shortcuts import render
from django.views.generic import TemplateView

from post_app.forms import PostForm

# Create your views here.

class HomeView(TemplateView):
    template_name = "home_app/home_main.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        data["post_form"] = PostForm()

        return data