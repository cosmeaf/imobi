from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth


def registro(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return HttpResponse(f'Bem-vindo')
        return render(request, 'registro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        if len(username.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0:
            messages.error(request, 'Favor preencher todos os campos')
            return redirect('registro')
        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(request, 'Usuário já cadastrado em sistema')
            return redirect('registro')

        try:
            user = User.objects.create_user(username=username,
                        email=email,
                        password=senha
                        )
            user.save()
            messages.success(request, 'Usuário Cadastrado com Sucesso!')
            return redirect('registro')
        except:
            return redirect('registro')

        # return HttpResponse(f'{username} " " {email} " " {senha}')


def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return HttpResponse(f'Bem-vindo')
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        usuario = auth.authenticate(username=username, password=senha)
        if not usuario:
            messages.error(request, 'Usuário e senha incorretos')
            return redirect('login')
        else:
            auth.login(request, usuario)
            return redirect('/')
        # return HttpResponse(f'{username} {senha}')

def logout(request):
    auth.logout(request)
    return redirect('login')