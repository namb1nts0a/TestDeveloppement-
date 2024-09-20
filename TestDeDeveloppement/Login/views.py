from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.template import loader
from django.urls import reverse
from django import template
from Login.form import CreateUserForm
from django.contrib import messages

# Create your views here.
def login(request):
    return render(request, "login.html")

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