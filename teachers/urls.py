from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.TeachersListView.as_view(), name='teachers'),
    url(r'^(?P<slug>[\w-]+)/$', views.TeacherDetailView.as_view(), name='teacher_detail'),
]
