from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('user/', include('users.urls')),
    path('products/', include('products.urls')),
]
