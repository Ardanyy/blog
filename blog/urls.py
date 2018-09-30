"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from app import views as vistas_app
from modelos import views as vistas_modelos

urlpatterns = [
    path("",vistas_app.inicio,name="inicio"),
     path("publicaciones/",vistas_modelos.post,name="post"),
    path("publicaciones/<int:id>/",vistas_modelos.detalle, name="detalle"),
    path('admin/', admin.site.urls),
      path('create/',vistas_modelos.post_new,name="create"),
     path("edit/<int:id>/",vistas_modelos.post_detalle,name="edit"),
]

