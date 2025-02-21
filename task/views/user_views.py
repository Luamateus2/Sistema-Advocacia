from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login,get_user_model
from django.contrib import messages

def add_user(request):
    if request.method == 'POST':
        name = request.POST.get('nome')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmar_senha')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'tasks/cadastro.html')

        User = get_user_model()

        if User.objects.filter(email=email).exists():
            messages.error(request, "This email is already in use.")
            return render(request, 'tasks/cadastro.html')

        try:
            new_user = User.objects.create_user(
                email=email, name=name, password=password)
            messages.success(
                request, "User created successfully! Please log in to continue.")
            return render(request, 'tasks/index.html')
        except Exception as e:
            messages.error(
                request, "An error occurred while creating the user. Please try again.")
            return render(request, 'tasks/cadastro.html')
    else:
        return render(request, 'tasks/cadastro.html')

def authenticate_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            print('Authenticated')
            return render(request,'tasks/login.html')
        else:
            messages.error(request, "Incorrect email or password.")
            return render(request, 'tasks/login.html')

    return render(request, 'tasks/login.html')
