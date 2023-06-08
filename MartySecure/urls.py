"""MartySecure URL Configuration

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
from django.contrib import admin
from django.urls import path
from Scanner import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('scanner/', views.port_scan, name='port_scan'),
    # path('api/results/', views.ValidatedResultList.as_view(),
    #      name='validated_result_list'),
    path('api/scan/', views.PortScanAPIView.as_view(), name='port_scan'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
]
