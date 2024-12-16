from django.urls import path
from . import views
urlpatterns = [
   	path('', views.index, name='home_page'),
    path('polit/', views.polit, name='polit'),
    path('sogl/', views.sogl, name='sogl')
]