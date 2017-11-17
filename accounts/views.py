from accounts.models import Token
from django.shortcuts import redirect, reverse
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.

def send_login_email(request):
    email = request.POST['email']
    token = Token.objects.create(email=email)
    # `request.build_absolute_uri` is one way to build a full URL
    # including teh domain name and the http(s) part, in Django
    url = request.build_absolute_uri(
        reverse('login') + '?token=' + str(token.uid)
    )
    message_body = f'Use this link to log in:\n\n{url}'
    send_mail(
        'Your login link for Superlists',
        message_body,
        'noreply@superlists',
        [email]
    )

    messages.success(
        request,
        "Check your email, we've sent you a link you can use to log in."
    )

    return redirect('/')


def login(request):
    return redirect('/')
