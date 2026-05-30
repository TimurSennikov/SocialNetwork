from django.shortcuts import redirect
from django.contrib.auth import login
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.http import JsonResponse, HttpRequest
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator
from django.template.loader import render_to_string

from friends_app.models import Friendship
from post_app.models import Post
from user_app.models import User, Profile

from .utils.friend_queries import get_users_by_section
from .utils.friend_actions import accept_friend_request, add_friend_request, delete_friendship, dismiss_recommendation

class FriendsView(LoginRequiredMixin, TemplateView):
    template_name = 'friends_app/friends_main.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sections'] = {
            'requests': {'title': 'Запити', 'users': get_users_by_section(user = self.request.user, section= 'requests')[:3]},
            'recommendations': {'title': 'Рекомендації', 'users': get_users_by_section(user = self.request.user, section= 'recommendations')[:6]},
            'friends': {'title': 'Всі друзі', 'users': get_users_by_section(user = self.request.user, section= 'friends')[:6]},
        }
        return context

# 
class FriendsSectionView(FriendsView):
    def get(self, request, section, *args, **kwargs):
        # Отримуємо потрібний список за назвою вкладки.
        users = get_users_by_section(request.user, section)
        # Розбиваємо людей на порції по 6 карток.
        page_obj = Paginator(users, 6).get_page(request.GET.get("page", 1))
        # Рендеримо тільки поточну порцію карток вибраної вкладки.
        html = render_to_string("friends_app/particles/friend_cards.html", 
                                {"users": page_obj.object_list, "section": section}, 
                                request=request
                                )
        # Повертаємо HTML поточної порції і ознаку наступної сторінки.
        return JsonResponse({"html": html, "has_next": page_obj.has_next()})
#  
class FriendActionView(LoginRequiredMixin, View):
    login_url = reverse_lazy('auth')
    
    def post(self, request, user_id, action, *args, **kwargs):
        other_user = User.objects.get(id= user_id)

        if action == 'add_redirect':
            return JsonResponse({'friend_html': reverse('profile_view', args= [other_user.id])})
        if action == 'add':
            return JsonResponse(add_friend_request(request.user, other_user))
        if action == 'dismiss':
            return JsonResponse(dismiss_recommendation(request.user, other_user))
        if action == 'accept':
            action_result = accept_friend_request(request.user, other_user)
            action_result['friend_html'] = render_to_string(
                'friends_app/particles/friend_cards.html',
                {'users': [action_result['friend']], 'section': 'friends'},
                request= request
            )
            del action_result['friend']
            
            return JsonResponse(action_result)
        # 
        return JsonResponse(delete_friendship(request.user, other_user))

class FriendProfile(LoginRequiredMixin, ListView):
    model = Post 
    template_name = 'friends_app/profile.html'
    context_object_name = 'posts'
    paginate_by = 5
    # 

    def get_context_data(self, **kwargs):
        puser = User.objects.get(id= self.kwargs.get('user_id'))
    
        context = super().get_context_data(**kwargs)
        context['profile_user'] = puser
        context['friendship'] = Friendship.objects.filter(from_user = self.request.user, to_user = puser).first() or Friendship.objects.filter(from_user = puser, to_user = self.request.user).first()

        return context
    
    def get_queryset(self):
        return Post.objects.filter(author_id = self.kwargs.get('user_id')).order_by('-created_at')

    def get(self, request, *args, **kwargs):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            page_number = request.GET.get('page')

            paginator = Paginator(Post.objects.filter(author_id=self.kwargs.get('user_id')).order_by('-created_at'), self.paginate_by)

            page_obj = paginator.get_page(page_number)
            if int(page_number) > paginator.num_pages:
                return JsonResponse({'success': False})
            return JsonResponse({
                'success': True,
                'html': render_to_string('post_app/particles/show_post.html', {'posts': page_obj.object_list})
            })
        
        return super().get(request, *args, **kwargs)