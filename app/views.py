from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from app.forms import FormContato, FormUsuario
from app.models import Pagina, Produto, Contato, Pedido
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):

    pagina = Pagina.objects.first()
    produtos = Produto.objects.all()

    contexto = {
        "pagina": pagina,
        "produtos": produtos
    }
    return render(request, "index.html", contexto)

#cadastro
def salvarUsuario(request):
    if request.method == "POST":
        form = FormUsuario(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Conta criada com sucesso!")
            return redirect("loginUsuario")
        
    else:
        form = FormUsuario()
    return render(request, "salvar-usuario.html",{"form":form})

#login

def loginUsuario(request):
    if request.POST:
        nome = request.POST.get('username')
        senha = request.POST.get('password')
        usuario = authenticate(request, username=nome, password=senha)

        if usuario is not None:
            login(request, usuario)
            request.session['nome_usuario'] = usuario.username

            return redirect('index')
        else:
            messages.error(request, "Usuário ou senha inválidos")

    return render(request, 'login.html')


#logoff
def logoutUsuario(request):
    logout(request)
    messages.success(request, "Você saiu da sua conta!")
    return redirect("index")

#contato
def salvarContato(request):
    if request.method == "POST":
        form = FormContato(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Mensagem enviada com sucesso!")
            return redirect("index")
        else:
            messages.error(request, "Verifique os campos e tente novamente!")
    else:
        form = FormContato()

    return redirect("index")



@login_required(login_url='loginUsuario')
def comprar(request, id_prod):
    produto = get_object_or_404(Produto, id=id_prod)
    return render(request, "comprar.html", {"produto":produto})


@login_required(login_url='loginUsuario')
def finalizarCompra(request, id_prod):
    if request.method == "POST":
        produto = get_object_or_404(Produto, id=id_prod)
        quantidade = int(request.POST.get("quantidade"))

        if quantidade > produto.estoque:
            messages.error(request, "Estoque insuficiente!")
            return redirect ("comprar", id_prod = id_prod)
        
        total = quantidade * produto.preco

        pedido = Pedido.objects.create(
            usuario = request.user if request.user.is_authenticated else None,
            produto = produto,
            quantidade = quantidade,
            total = total
        )
        #produto.estoque -= quantidade
        produto.save()
        return render(request, "pedido_finalizado.html", {"pedido":pedido})
    return redirect("index")


@login_required(login_url='loginUsuario')
def perfil(request):
    usuario = request.user
    pedidos = Pedido.objects.filter(usuario=usuario).order_by("-data")
    return render(request, "perfil.html", {"usuario":usuario, "pedidos":pedidos})