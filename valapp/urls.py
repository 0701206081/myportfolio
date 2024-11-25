
from django.contrib import admin
from django.urls import path
from valapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('', views.contact, name='contact'),


]
