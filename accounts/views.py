import uuid
import sys
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.urls import reverse
# from accounts.models import Token, ListUser
from accounts.models import Token

# Create your views here.
def send_login_email(request):
    email = request.POST['email']
    token = Token.objects.create(email=email)
    # print(type(send_mail))
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
#     print('login view', file=sys.stderr)
#     uid = request.GET.get('uid')
#     print("uid:",uid)
#     # print(type(uid))
#     user = authenticate(uid=uid)
#     print(authenticate(uid=uid))
#     if user is not None:
#         auth_login(request, user)
#     return redirect('/')

# def logout(request):
#     auth_logout(request)
#     return redirect('/')