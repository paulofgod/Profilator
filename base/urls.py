from django.urls import path
from . import views
from .views import logout_view
app_name="base"
urlpatterns = [
    path('home/', views.home, name="home"),
    path('posts/', views.posts, name="posts"),
    path('privacy_policy/', views.privacy, name="privacy"),
    path('post/', views.post, name="post"),
    path('term_of_use/', views.terms, name="terms"),
    path('profile/', views.profile, name="profile"),
    path('update_profile/', views.update_profile, name="update_profile"),
    path('login/', views.login_user, name="login"),
    path('logout/', logout_view, name='logout'),

]

