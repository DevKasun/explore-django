from django.http import HttpResponse

def profile_view(request):
    return HttpResponse("User Profile page")

def profile_settings_view(request):
    return HttpResponse("Profile settings page")