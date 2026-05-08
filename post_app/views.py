from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import PostForm
# Create your views here.

class MyPostsView(TemplateView):
    template_name = 'post_app/post_main.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        data["post_form"] = PostForm()

        return data