from django.http import HttpResponse

def index(request):
    return HttpResponse("Accueil du catalogue ✅")

def ping(request):
    return HttpResponse("Catalogue OK ✅")
