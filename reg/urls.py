from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.register, name='reg_home'),  # Пример маршрута для домашней страницы reg
    path('main/', include('main.urls'), name='home_page'),
    path('login/', auth_views.LoginView.as_view(template_name='reg/log.html'), name='log_page'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]