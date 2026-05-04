from django.shortcuts import render
from django.views.generic import TemplateView , FormView
from .forms import MessageForm
# Create your views here.

class ChatView(
        FormView, 
        # TemplateView
    ):
    template_name = "chat_app/chat.html"
    form_class = MessageForm
    # extra_context = {
    #     "form": MessageForm()
    # }
    

