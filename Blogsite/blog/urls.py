from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import PostList

app_name = 'blog'

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
]
