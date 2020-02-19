"""apisix_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path(r'api/v1/api-token-auth/', obtain_jwt_token),
    path(r'api/v1/upstreams/', include('upstreams.urls', namespace="upstreams")),
    path(r'api/v1/tenant/', include('tenant.urls', namespace="tenant")),
    path(r'api/v1/ssl/', include('sni.urls', namespace="sni")),
    path(r'api/v1/plugins/', include('plugins.urls', namespace="plugins")),
    path(r'api/v1/users/', include('users.urls', namespace="users")),
    path(r'api/v1/routes/', include('routes.urls', namespace="routes")),
    path(r'api/v1/consumers/', include('consumers.urls', namespace="consumers")),
    path(r'api/v1/services/', include('services.urls', namespace="services")),
    path(r'api/v1/schema/', include('schema.urls', namespace="schema")),
]
