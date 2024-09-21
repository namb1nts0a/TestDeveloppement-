from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.template import loader
from django.urls import reverse
from django import template
from Login.form import CreateUserForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.
def login(request):
    form = UserLoginForm()
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, "Connexion reussie")
                return redirect("/")
            else:
                messages.error(request, "Email ou mot de passe incorrect")
        else:
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")

    context = {
        'form' : form
    }
    return render(request, "login.html", context)

def signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            print("save", messages)
            messages.success(request, "Votre compte a ete cree")
            return redirect('/login/')
        else:
            print("unsave", messages)
            messages.error(request, "il y a une erreur")

    context = {
        'form' : form
    }

    return render(request, "signup.html", context)


def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('500.html')
        return HttpResponse(html_template.render(context, request))