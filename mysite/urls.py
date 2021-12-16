"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, path
from lovejoy import views as ljviews
from django.contrib.auth import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', ljviews.home),
    path('signup/', ljviews.signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('home/', ljviews.home, name='home'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('lovejoy/', include('lovejoy.urls')),
    path('admin/', admin.site.urls),
    path('account_activation_sent/', ljviews.account_activation_sent, name='account_activation_sent'),
    path('activate/<uidb64>/<token>/', ljviews.activate, name='activate'),
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('evaluation/', ljviews.evaulation_view, name='evaluation'),
    path('staff/', ljviews.staff_view, name='staff'),
] + [
    path('captcha/', include('captcha.urls')),
]
