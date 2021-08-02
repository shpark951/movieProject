from django.urls import path
from bookmark.views import *
app_name = 'bookmark'
urlpatterns = [
 path('', BookmarkListView.as_view(), name='index'),
 path('<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
 # Example: /bookmark/add/
 path('add/', BookmarkCreateView.as_view(), name="add"),
 # Example: /bookmark/change/
 path('change/', BookmarkChangeListView.as_view(), name="change"),


 # Example: /bookmark/99/update/
 path('<int:pk>/update/', BookmarkUpdateView.as_view(), name="update"),
 # Example: /bookmark/99/delete/
 path('<int:pk>/delete/', BookmarkDeleteView.as_view(), name="delete"),


]