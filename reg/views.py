from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm

# Вьюха для регистрации пользователя
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт для {username} был успешно создан!')
            return redirect('account_home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'reg/reg.html', {'form': form})

# Вьюха для аутентификации
def login_page(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('account_home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'reg/log.html', {'form': form})
