from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.TeacherListView.as_view(), name='teachers'),
    url(r'^teacher/(?P<pk>\d+)/$', views.TeacherDetailView.as_view(), name='teacher_detail'),
    url(r'^filter/$', views.TeacherFilterView.as_view(), name='teachers'),
]
