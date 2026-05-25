from django.shortcuts import render
from django.views.generic import TemplateView , FormView
from .forms import MessageForm

from friends_app.utils.friend_queries import get_users_by_section

from user_app.models import User

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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["contacts"] = User.objects.all()
        print(get_users_by_section(self.request.user, "friends"))
        
        return context