from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from blog.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from accounts.views import OwnerOnlyMixin
# ListView
class PostListView(ListView):
 model = Post
 template_name = 'blog/post_all.html' # 템플릿 파일명 변경
 context_object_name = 'posts' # 컨텍스트 객체 이름 변경(object_list)
 paginate_by = 2 # 페이지네이션, 페이지당 문서 건 수
# DetailView
class PostDetailView(DetailView):
 model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
 model = Post
 fields = ['title', 'description', 'content']
 success_url = reverse_lazy('blog:index')
 
 def form_valid(self, form):
    form.instance.owner = self.request.user
    return super().form_valid(form)

class PostUpdateView(OwnerOnlyMixin, UpdateView):
 model = Post
 fields = ['title', 'description', 'content']
 success_url = reverse_lazy('blog:index')

class PostDeleteView(OwnerOnlyMixin, DeleteView) :
 model = Post
 success_url = reverse_lazy('blog:index')
 
 def get(self, *args, **kwargs):
    return self.post(*args, **kwargs)
