from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='index'),
    path('create/', views.create_blog, name='create_blog'),
    path('<slug:slug>/', views.post_detail, name='detail'),
        path('blogs/<int:post_id>/delete/', views.delete_post, name='delete_post'),

]