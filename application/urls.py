from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    # path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register_user, name="register"),
    path('logout/', views.logout_view, name='logout'),
    # path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    # path('ariza_yuborish/', views.ariza_yuborish, name='ariza_yuborish'),
]
