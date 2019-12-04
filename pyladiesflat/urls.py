from django.contrib import admin
from django.urls import path
from pyladies import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.base_view, name='base'),
    path('schedule/', views.schedule_view, name='schedule'),
    path('publications/', views.publication_view, name='publications'),
    path('resources/', views.resource_view, name='resources'),
    path('partners/', views.partner_view, name='partners'),
]
