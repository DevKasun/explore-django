from django.urls import path
from users.views import profile_view, profile_settings_view

urlpatterns = [
    path('profile', profile_view),
    path('profile/settings', profile_settings_view),
]