from django.contrib.auth import views as auth_views
from django.urls import include, path

from . import views


app_name = 'core'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('group/<group_id>', views.Group.as_view(), name='group'),
    path('group/create/', views.GroupCreate.as_view(), name='group_create'),
    path('group/update/<group_id>', views.GroupUpdate.as_view(), name='group_update'),
    path('group/delete/<group_id>', views.GroupDelete.as_view(), name='group_delete'),
    path('student/create/', views.StudentCreate.as_view(), name='student_create'),
    path('student/update/<student_id>', views.StudentUpdate.as_view(), name='student_update'),
    path('student/delete/<student_id>', views.StudentDelete.as_view(), name='student_delete'),
]
