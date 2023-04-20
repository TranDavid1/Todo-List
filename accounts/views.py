import uuid
import sys
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout
# from accounts.models import Token, ListUser
from accounts.models import Token

# Create your views here.
def send_login_email(request):
    email = request.POST['email']
    # print(type(send_mail))
    send_mail(
        'Your login link for Superlists', 
        'body text tbc',
        'noreply@superlists', 
        [email]
    )
    messages.success(
        request,
        "Check your email, we've sent you a link you can use to log in."
    )
    # uid = str(uuid.uuid4())
    # Token.objects.create(email=email, uid=uid)
    # # ListUser.objects.create(email=email)
    # print('saving uid', uid, 'for email', email, file=sys.stderr)
    # url = request.build_absolute_uri(f'/accounts/login?uid={uid}')
    # send_mail(
    #     'Your login link for Superlists',
    #     f'Use this link to log in:\n\n{url}',
    #     'noreply@superlists',
    #     [email],
    # )
    # return render(request, 'login_email_sent.html')
    return redirect('/')

# def login(request):
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