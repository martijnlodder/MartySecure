from django.urls import path, include
from . import views
from .views import ValidatedResultList
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from allauth.account.views import LoginView, LogoutView
from .views import mfa_setup

urlpatterns = [
    path('port_scan/', views.port_scan, name='port_scan'),
    path('api/results/', ValidatedResultList.as_view(),
         name='validated_result_list'),

    path('accounts/', include('allauth.urls')),
    path('accounts/login/', LoginView.as_view(), name='account_login'),
    path('accounts/logout/', LogoutView.as_view(), name='account_logout'),
    path('accounts/mfa/setup/',
         TemplateView.as_view(template_name='mfa/setup.html'), name='mfa_setup'),
    path('accounts/mfa/login/',
         auth_views.LoginView.as_view(template_name='mfa/login.html'), name='mfa_login'),
    path('accounts/mfa/login/setup/',
         TemplateView.as_view(template_name='mfa/setup.html'), name='mfa_setup'),
    path('accounts/mfa/login/',
         auth_views.LoginView.as_view(template_name='mfa/login.html'), name='mfa_login'),
    path('accounts/mfa/login/authenticate/', auth_views.LoginView.as_view(
        template_name='mfa/authenticate.html'), name='mfa_authenticate'),
    path('accounts/mfa/setup/', mfa_setup, name='mfa_setup'),
]
