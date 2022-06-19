from .models import Feature
from django.shortcuts import render


# Create your views here.
def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})
