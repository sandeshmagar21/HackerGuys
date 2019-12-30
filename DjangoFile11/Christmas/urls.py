from django.contrib import admin
from django.urls import path
from .views import *
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hellopage/',view_helloworld),
    path('index/',view_indexpage)
]