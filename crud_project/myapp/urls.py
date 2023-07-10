from django.urls import path
from .views import (RegisterView,
                    LoginView,
                    LogoutView,
                    PostListView,
                    PostDetailView,
                    SomeView,
                    UserListView)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='READ/DELETE/UPDATE'),
    path('login-status/', SomeView.as_view()),
    path('list/', UserListView.as_view(), name='registered-users-list'),
]
