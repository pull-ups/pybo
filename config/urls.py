from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from pybo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')), 
    path('common/', include('common.urls')),
    path('', views.index, name='index'),  # '/' 에 해당되는 path

    
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
]
if settings.DEBUG:
    print("DEbug")
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]