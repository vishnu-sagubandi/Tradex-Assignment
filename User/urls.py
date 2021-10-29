from django.urls import path, include
from .views import home, UserSignupView, UserLoginView, logout_view, create_post_view

urlpatterns = [
    path('', home, name='home'),
    path('user/register/', UserSignupView, name='signup'),
    path('user/login/', UserLoginView, name='login'),
    path('logout/', logout_view, name='logout'),
    path('post/create/', create_post_view, name='create-post'),
]
