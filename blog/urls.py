from django.urls import path, re_path
from blog.views import *
app_name = 'blog'
urlpatterns = [
 path('', PostListView.as_view(), name='index'),
 path('<int:pk>/', PostDetailView.as_view(), name='detail'),
 # Example: /blog/add/
 path('add/', PostCreateView.as_view(), name="add"),
 # Example: /blog/99/update/
 path('<int:pk>/update/', PostUpdateView.as_view(), name="update"),
 # Example: /blog/99/delete/
 path('<int:pk>/delete/', PostDeleteView.as_view(), name="delete"),
]