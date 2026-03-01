from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('success/', views.success, name='success'),
    path('history/', views.history, name='history'),   # My Bookings page
    path('account/', views.account, name='account'),   # Account page
    path('about/', views.about, name='about'),         # About page
    path('contact/', views.contact, name='contact'),   # Contact page
    path('signup/', views.signup, name='signup'),     # Signup page
]