from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/schedule/', permanent=True)),
    path('schedule/', include('schedule.urls')),
    path('teachers/', include('teachers.urls')),
]
