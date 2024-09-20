from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django import template

# Create your views here.
def login(request):
    return render(request, "login.html")


def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('500.html')
        return HttpResponse(html_template.render(context, request))