from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/lessons/', include('schedule.urls')),
    path('api/v1/teachers/', include('teachers.urls')),
    path('api/v1/subjects/', include('subjects.urls')),
    path('api/v1/groups/', include('groups.urls')),
]
