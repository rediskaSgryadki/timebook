from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='account_home'),  # Пример маршрута для домашней страницы reg
    path('main/', include('main.urls'), name='home_page'),
    path('zametka/', views.create_note, name='zametka'),
    path('kalendar/', views.kalendar, name='kalendar'),
     path('zametka/<int:id>/', views.zametka_detail, name='zametka_detail'),
]
