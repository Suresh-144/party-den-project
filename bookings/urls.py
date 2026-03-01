from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('success/', views.success, name='success'),
    path('history/', views.history, name='history'),
    path('account/', views.account, name='account'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')), # Built-in login/logout
]