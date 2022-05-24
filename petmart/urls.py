"""petmart URL Configuration

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
#rom xml.etree.ElementInclude import include
from .import views
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header="PetMart Admin"
admin.site.site_title="PetMart Admin Panel"
admin.site.index_title="Welcome to PetMart Admin Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/',include("shop.urls")),
    path('blog/',include("blog.urls")),
    path("",views.index,name="homePage"),
]+static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
 