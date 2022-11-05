from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path("", BlogListView.as_view(), name="home"), 
    path("create_post", BlogCreateView.as_view(), name="create_post")
]