from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('materials/', views.manage_materials_view, name='manage_materials'),
    path('vehicles/', views.manage_vehicles_view, name='manage_vehicles'),
    path('rentals/', views.manage_rentals_view, name='manage_rentals'),
    path('main-page/', views.main_page_view, name='main-page'),
    path('registration/', views.registration_page_view, name='registration'),
]