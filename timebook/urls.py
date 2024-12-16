from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('reg/', include('reg.urls')),
    path('account/', include('account.urls')),
]
