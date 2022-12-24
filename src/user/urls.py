from django.urls import path
#from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
  path('register/', views.register, name='register'),
 # path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
  path('login/', views.login_user, name='login'),
  path('logout/', views.logout_user, name='logout'),
  #path('logout/', LogoutView.as_view(template_name='user/logout.html'), name='logout'),
  path('profile/', views.profile, name='profile'),
]
