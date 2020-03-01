from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            subject = request.POST.get('subject','')
            content = request.POST.get('content','')

            # Enviamos el correo y redireccionamos
            email = EmailMessage(
                #asunto,
                "Udrizar Hermanos, nuevos mensaje de contacto",
                #cuerpo,
                "De {} <{}>\n\nAsunto: {}\n\nEscribió:\n\n{}".format(name, email, subject, content),
                #email_origen
                "no-responder@inbox.mailtrap.io",
                #email_destino,
                ["lautaropoletto@outlook.com","lautaropoletto@gmail.com"],
                reply_to=[email]
            )

            try:
                # todo ha ido bien
                email.send()
                return redirect(reverse('contact')+"?ok")
            except:
                #Algo no ha ido bien
                return redirect(reverse('contact')+"?fail")    
    return render(request, "contact/contact.html", {'form':contact_form})