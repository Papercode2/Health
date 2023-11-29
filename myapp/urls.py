from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='index'),
  
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name="home"),
    path('appointment/', views.appointment, name="appointment"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('logout/', views.logout, name="logout"),
    path('pay/', views.pay, name="pay"),
    path('approval/', views.approval, name='approval'),
    path('download_receipt/<int:access_token_id>/',views.download_receipt, name='download_receipt'),
    path('daraja/stk_push', views.stk_push_callback, name='stk_push_callback'),
    path('success/', views.success, name='success'),
    path('accounts/settings/', views.settings, name='settings'),
    path('bookings/', views.bookings, name='bookings'),
    path('doctors/', views.doctors, name='doctors'),
    path('sessions/', views.sessions, name='sessions'),
    path('adminstrator/', views.adminstrator, name='adminstrator'),
    path('save_profile/', views.save_profile, name='save_profile'),
]
