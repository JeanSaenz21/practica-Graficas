from django.shortcuts import render

# Create your views here.


def graficas(request):
    return render(request, "practica_graficas/index.html")