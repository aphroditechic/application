"""
URL configuration for board_game project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from games import views as game_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', game_views.home, name='home'),  # Home page
    path('inventory/', game_views.inventory, name='inventory'),  # Inventory page
    path('accounts/', include('django.contrib.auth.urls')),  # For built-in auth URLs like login, logout
    path('signup/', game_views.signup, name='signup'),  # Sign-up page
    path('logout/', LogoutView.as_view(), name='logout'),  # Custom logout URL
    path('accounts/profile/', game_views.profile, name='profile'),  # Profile page URL
]
