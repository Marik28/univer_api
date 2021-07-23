from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.SubjectListView.as_view()),
    url(r'^subject/(?P<pk>\d+)/$', views.SubjectDetailAPIView.as_view()),
]
