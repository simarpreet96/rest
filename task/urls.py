from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include
from snippets import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('snippets.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
