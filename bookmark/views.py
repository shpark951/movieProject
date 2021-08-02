from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from bookmark.models import Bookmark
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from accounts.views import OwnerOnlyMixin

class BookmarkListView(ListView):
 model = Bookmark
class BookmarkDetailView(DetailView):
 model = Bookmark

class BookmarkCreateView(LoginRequiredMixin, CreateView):
 model = Bookmark
 fields = ['title', 'url'] # form 클래스에서 사용할 필드form 클래스 자동생성
 success_url = reverse_lazy('bookmark:index')
 
 def form_valid(self, form): # post 요청시 form의 유효성 검사 통과되면 호출
 # form.instance : 폼 정보를 기반으로 생성된 모델 인스턴스
    form.instance.owner = self.request.user # 로그인 사용자 정보
    return super().form_valid(form) # 모델 인스턴스 저장

class BookmarkChangeListView(LoginRequiredMixin, ListView): 
 template_name = 'bookmark/bookmark_change_list.html' 
 
 def get_queryset(self):
    return Bookmark.objects.filter(owner=self.request.user)

class BookmarkUpdateView(OwnerOnlyMixin, UpdateView): 
 model = Bookmark 
 fields = ['title', 'url'] # 폼 모델에 사용할 필드  폼 모델 자동 생성
 success_url = reverse_lazy('bookmark:change') 

class BookmarkDeleteView(OwnerOnlyMixin, DeleteView): 
 model = Bookmark 
 success_url = reverse_lazy('bookmark:change')
 def get(self, *args, **kwargs):
   return self.post(*args, **kwargs)