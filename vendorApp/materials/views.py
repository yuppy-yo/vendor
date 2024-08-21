from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['userLogin']
        password = request.POST['userPassword']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Вход выполнен успешно!")
            return redirect('home')
        else:
            messages.error(request, "Неверный логин или пароль.")
    return render(request, 'login.html')

def home_view(request):
    return render(request, 'home.html')

def main_page_view(request):
    return render(request, 'main-page.html')

def registration_page_view(request):
    return render(request, 'registration.html')

def logout_view(request):
    logout(request)
    messages.success(request, "Вы успешно вышли из системы.")
    return redirect('login')

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')

@login_required
@permission_required('materials.view_material')
def manage_materials_view(request):
    return render(request, 'manage_materials.html')

@login_required
@permission_required('materials.view_vehicle')
def manage_vehicles_view(request):
    return render(request, 'manage_vehicles.html')

@login_required
@permission_required('materials.view_rental')
def manage_rentals_view(request):
    return render(request, 'manage_rentals.html')
