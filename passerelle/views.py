from django.http import HttpResponse

def passerelle_endpoint(request):
    # Logique de redirection vers les microservices
    return HttpResponse("Passerelle Endpoint")
