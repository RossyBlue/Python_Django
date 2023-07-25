from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import VehiculoForm, RegistroUsuarioForm

from django.http import HttpResponse, HttpResponseRedirect,HttpResponseForbidden
from tokenize import PseudoExtras
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType
from .models import VehiculoModel
from django.contrib.auth.decorators import login_required




# Create your views here.

def indexView(request):
    return render(request, 'index.html', {})



@login_required
def addVehiculo(request):
    #if not request.user.has_perm('vehiculo.add_Vehiculo'):   #Utilizar para denegar acceso en caso de ser necesario 
        #return HttpResponseForbidden()
    
    if request.method == 'POST':
        form = VehiculoForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            form = VehiculoForm()
            messages.success(request, '¡Los datos se han procesado exitosamente!')
            return redirect ('index')
    else:
        form = VehiculoForm()

    return render(request, 'addform.html', {'form' : form})
    

def registro_view(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            content_type = ContentType.objects.get_for_model(VehiculoModel)
            visualizar_catalogo = Permission.objects.get(codename='visualizar_catalogo', content_type=content_type)
            
            user = form.save()

            user.user_permissions.add(visualizar_catalogo)

            login(request, user)
            messages.success(request, "Usuario registrado exitosamente.")
            return HttpResponseRedirect('/')
        messages.error(request, "Registro inválido. Algunos datos incorrectos. Verifique")

    form = RegistroUsuarioForm()
    context = { "register_form": form}
    return render(request, "registro.html", context)

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Iniciaste sesión como: {username}")
                return HttpResponseRedirect("/")
            else:
                messages.error(request, "¡Username o password inválido!")
        else:
            messages.error(request, "¡Username o password inválido!")


    form = AuthenticationForm()
    context = { "login_form": form}
    return render(request, "login.html", context)

@login_required
def listar_vehiculo(request):
    vehiculos = VehiculoModel.objects.all()
    context = { 'lista_vehiculos' : vehiculos }
    return render(request, 'lista.html', context)

def logout_view(request):
    logout(request)
    return redirect('index')

