from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jetemi95scrumy/', include('jetemi95scrumy.urls')),
]