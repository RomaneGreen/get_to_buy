from django.urls import path, include
from riverrapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('loginout/', auth_views.login,name='login'),
    path('login/', auth_views.logout,name='logout')
]
