from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage    # Se utiliza para armar la estructura de un mensaje

# Create your views here.
def contact(request):
    contact_form = ContactForm()                          #Creamos la plantila vacia

    if request.method == 'POST':                          # comprobamos si se ha enviado algun dato mediante el metodo POST
        contact_form = ContactForm(data=request.POST)     # si se ha enviado algun dato rellenamos la plantilla con esta informacion
        if contact_form.is_valid():
            name = request.POST.get ('name','')
            email = request.POST.get ('email','')
            content = request.POST.get ('content','')
            # Enviamos correo y redireccionamos
            email = EmailMessage(
                "La cafetiera: Nuevo mensaje de contacto",                      #asunto
                "De {} <{}>\n\nEscribió:\n\n{}".format (name,email,content),    #cuerpo
                "no-contenstar@inbox.mailtrap.io",                              #email_origen
                ["nicogette6@gmail.com"],                                       #email_destino
                reply_to=[email]
            )
            try:
                email.send ()
                # Ha salido todo bien y lo redireccionamos a OK
                return redirect (reverse('contact') + '?ok')
            except:
                # Algo no ha salido bien y lo redireccionamos a FAIL
                return redirect (reverse('contact') + '?fail')

    return render (request, 'contact/contact.html', { 'form': contact_form })