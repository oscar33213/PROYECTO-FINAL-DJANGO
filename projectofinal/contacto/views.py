from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage
# Create your views here.


def Vista_Contacto(request):
    forulario_contacto = FormularioContacto() #INSTANCIAMOS LA CLASE
    
    if request.method == "POST":
        formulario_contacto = FormularioContacto(data=request.POST)
        if  formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")
            
            
            email = EmailMessage(f"Mensaje desde App Django", "Usuario {}. Dirección {}. Mensaje:\n\n {}". format(nombre, email,contenido),
                        "",["oshill13@outlook.es"])
            
            
            try:
                email.send()
            
                return redirect("/contacto/?valido")
            
            
            except:
                
                return redirect("/contacto/?novalido")
                
    return render (request, "contacto/contacto.html", {"miFormulario": forulario_contacto})