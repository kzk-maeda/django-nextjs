"""backend URL Configuration

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
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework import permissions
from rest_framework.renderers import OpenAPIRenderer
from django.views.generic.base import TemplateView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView

def openapi_schema_path():
    view = get_schema_view(
        title="Jobbee API",
        description="[DFR標準] OpenAPI document",
        version="1.0.0",
        public=True,
        urlconf='backend.urls',
        renderer_classes=[OpenAPIRenderer],
        permission_classes=(permissions.AllowAny,),
    )
    
    return view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('job.urls')),
    path('api/', include('account.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/verify', TokenVerifyView.as_view()),
    path('openapi-schema/', openapi_schema_path(), name='openapi-schema'),
]

handler404 = 'utils.error_views.handler404'
handler500 = 'utils.error_views.handler500'

