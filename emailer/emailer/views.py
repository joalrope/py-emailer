from django.shortcuts import render
from django.shortcuts import redirect

from django.core.mail import send_mail


def index(request):
    return render(request, 'index.html', {})


def mail(request):

    subject = 'prueba de correo'
    message = 'Desde un correo enviado via django'
    from_email = 'labsecureemailtest@sucresecure.com'
    to_emails = ['joalrope@gmail.com']

    send_mail(subject, message, from_email, to_emails, fail_silently=False)

    return redirect('index')
