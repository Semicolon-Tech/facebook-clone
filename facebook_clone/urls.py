"""facebook_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from dj_rest_auth.views import PasswordResetConfirmView
from django.contrib import admin
from django.urls import path, include, re_path

api_prefix = "api/v1"

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'{api_prefix}/register/', include('dj_rest_auth.registration.urls')),
    path(f'{api_prefix}/', include('dj_rest_auth.urls')),
    path(f'{api_prefix}/', include("allauth.account.urls")),

    re_path(
        rf'^{api_prefix}/password/reset/confirm/'
        r'(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$',
        PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
]
