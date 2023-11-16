from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import signup, Loginn, Logoutt, index
from .import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', views.Loginn, name='login'),
    path('logout/', views.Logoutt, name='logout'),
    path('index/', login_required(index), name='index'),
]