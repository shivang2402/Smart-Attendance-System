from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/logout/')),
    path('accounts/', include('django.contrib.auth.urls')),
    re_path(r'^attendance_submit/$', views.attendance_submit, name='Master-attendance_submit'),
    re_path(r'^login_submit/$', views.user_login, name='Master-login_submit'),
    re_path(r'^contact/$', views.contact, name='Master-contact'),
    re_path(r'^view/$', views.view_attendance, name='Master-view'),
    re_path(r'^login/$', views.login_module, name='Master-login'),
    re_path(r'^logout/$', views.redirect_home, name='Master-logged_out'),
    path('mark_attendance/<str:course_id>/', views.mark_attendance, name='Master-mark_attendance'),
    path('timetable/<str:dep_id>/<str:sem>/', views.timetable, name='Master-timetable'),
    path('view/<str:course_id>/', views.course_view, name='Master-course_view'),
    re_path(r'^contact_submit/$', views.contact_submit, name='Master-contact_submit'),
    re_path(r'^$', views.home, name='Master-home'),
]
