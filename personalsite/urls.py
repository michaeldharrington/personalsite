from django.contrib import admin
from django.urls import path
from public.views import HomeView, AboutView, ResView, ProjectListView, ProjectView


from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from public import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('about/resume/', ResView.as_view(), name='resume'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('projects/<int:pk>/', ProjectView.as_view(), name='project-detail'),
    url(r'^projectlist/$', views.ProjectList.as_view()),
    url(r'^projectdetail/(?P<pk>[0-9]+)/$', views.ProjectDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
