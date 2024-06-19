from django.shortcuts import render

def aviso_legal(request):
    return render(request, "legal/legal.html")
