from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def voos_view(request):

    context= {
        'voos': Voo.objects.all().order_by('origem')
    }
    return render(request, 'voos/voos.html', context)


def voo_view(request, voo_id):

    voo = Voo.objects.get(id=voo_id)
    context= {
        'voo': voo,
        'passageiros': voo.passageiros.all(),
        'nao_passageiros': Passageiro.objects.exclude(voos__in = [voo])
    }

    return render(request, 'voos/voo.html', context)


def passageiros_view(request):

    context= {
        'passageiros': Passageiro.objects.all().order_by('nome')
    }
    return render(request, 'voos/passageiros.html', context)


def passageiro_view(request, passageiro_id):

    passageiro = Passageiro.objects.get(id=passageiro_id)
    context= {
        'passageiro': passageiro
    }

    return render(request, 'voos/passageiro.html', context)


@login_required
def adicionar_passageiro_view(request, voo_id):
    voo = Voo.objects.get(id=voo_id)

    if request.method == 'POST':
        passageiro = Passageiro.objects.get(id=request.POST['passageiro'])
        voo.passageiros.add(passageiro)

    context= {
        'voo': voo,
        'passageiros': voo.passageiros.all(),
        'nao_passageiros': Passageiro.objects.exclude(voos__in = [voo])
    }

    return render(request, 'voos/voo.html', context)

@login_required
def remover_passageiro_view(request, voo_id, passageiro_id):
    voo = Voo.objects.get(id=voo_id)
    passageiro = Passageiro.objects.get(id = passageiro_id)

    voo.passageiros.remove(passageiro)
        
    context= {
        'voo': voo,
        'passageiros': voo.passageiros.all(),
        'nao_passageiros': Passageiro.objects.exclude(voos__in = [voo])
    }

    return render(request, 'voos/voo.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,
                           username=username,
                           password=password)
        
        if user is not None:
            login(request, user)
            return redirect('voos')
        else:
            return render(request, 'voos/login.html', {
                'message': 'Credenciais invalidas'
            })
    return render(request, 'voos/login.html')



def logout_view(request):
    logout(request)
    return redirect('voos')

