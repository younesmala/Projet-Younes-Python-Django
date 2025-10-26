from django.http import HttpResponse

def ping(request):
    return HttpResponse("Catalogue OK ✅")
