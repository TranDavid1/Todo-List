from accounts.models import User, Token

class PasswordlessAuthenticationBackend(object):

    def authenticate(self, request, email=None):
        # code doesn't seem to work
        # try:
        #     token = Token.objects.get(uid=uid)
        #     return User.objects.get(email=token.email)
        # except User.DoesNotExist:
        #     return User.objects.create(email=token.email)
        # except Token.DoesNotExist:
        #     return None
        try:
            token = Token.objects.get(uid=request.GET.get('token'))
            return User.objects.get(email=token.email)
        except User.DoesNotExist:
            return User.objects.create(email=token.email)
        except Token.DoesNotExist:
            return None
        
    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None