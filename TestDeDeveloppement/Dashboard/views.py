from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

# decorateur pour la views inaccessible si on se log pas et rediriger vers la page login
@login_required(login_url='/login/')
#gerer la mise en cache du vue par les navigateurs
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    return render(request, "index.html")