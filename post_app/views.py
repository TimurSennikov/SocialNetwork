from django.shortcuts import render
from django.views.generic import TemplateView, ListView, FormView

from django.template.loader import render_to_string

from django.urls import reverse_lazy

from django.http import JsonResponse

from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import PostForm
from .models import Post

from django.core.paginator import Paginator

# Create your views here.

class MyPostsView(TemplateView):
    template_name = 'post_app/post_main.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        data["post_form"] = PostForm()

        return data

class PostListView(LoginRequiredMixin, ListView):
    template_name = 'post_app/post_main.html'
    paginate_by = 5
    login_url = reverse_lazy('auth')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['post_creation_form'] = PostForm()
        context['posts'] = Post.objects.filter(author_id = self.request.user.id)[:self.paginate_by]

        return context
    
    def get_queryset(self):
        return Post.objects.filter(author_id = self.request.user.id)
    
    def get(self, request, *args, **kwargs):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            queryset = self.get_queryset()
            paginator = Paginator(queryset, self.paginate_by)
            try:
                page = int(request.GET.get('page', 1))
            except (TypeError, ValueError):
                page = 1
            page_obj = paginator.get_page(page)

            if page > paginator.num_pages:
                return JsonResponse({'success': False})

            return JsonResponse({
                'success': True,
                'html': render_to_string('post_app/particles/show_post.html', {'posts': page_obj.object_list})
            })
        return super().get(request, *args, **kwargs)

class PostCreateView(LoginRequiredMixin, FormView):
    form_class = PostForm
    success_url = reverse_lazy('post')
    login_url = reverse_lazy('auth')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        if self.request.method == 'POST':
            kwargs['links'] = self.request.POST.getlist('links')
            print(kwargs['links'], "links")
            kwargs['images'] = self.request.FILES.getlist('images')

        return kwargs

    def form_valid(self, form: PostForm):
        post = form.save(author = self.request.user)

        return JsonResponse(
            {
                'success': True,
                'message': 'Публікацію створено успішно',
                'redirect_url': str(self.success_url),
                'post_id': post.id
            }
        )

    def form_invalid(self, form: PostForm):
        print(form.errors.get_json_data(), "form errors")
        return JsonResponse(
            {
                "success" : False,
                'errors': form.errors.get_json_data()
            },
            status = 400
        )