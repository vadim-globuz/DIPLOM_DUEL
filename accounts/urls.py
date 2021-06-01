from django.contrib.auth import views
from django.urls import path
from .views import SignUpView, register
app_name = 'login'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', register, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]