"""
URL configuration for todolist project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from bboard.views import BbIndexView, BbCreateView, BbDeleteView, BbDetailView, BbEditView, about_page, contacts_page

app_name = 'bboard'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BbIndexView.as_view(), name='index'),
    path('about/', about_page, name='about'),
    path('contacts/', contacts_page, name='contacts'),
    path('add/', BbCreateView.as_view(), name='add'),
    path('detail/<int:pk>', BbDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', BbDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', BbEditView.as_view(), name='update')
]
