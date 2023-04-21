from django.test import TestCase
from unittest.mock import patch, call
from accounts.models import Token
# import accounts.views

class SendLoginEmailViewTest(TestCase):

    def test_redirects_to_home_page(self):
        response = self.client.post('/accounts/send_login_email', data={
            'email': 'john@example.com'
        })
        self.assertRedirects(response, '/')

    # patch decorator is equivalent of replacing send_mail in accounts.views
    # automatically replaces target with a mock and puts original object back after
    @patch('accounts.views.send_mail')
    # patch injects mock object as an argument
    def test_sends_mail_to_address_from_post(self, mock_send_mail):
        self.client.post('/accounts/send_login_email', data={
            'email': 'john@example.com'
        })

        self.assertEqual(mock_send_mail.called, True)
        (subject, body, from_email, to_list), kwargs = mock_send_mail.call_args
        self.assertEqual(subject, 'Your login link for Superlists')
        self.assertEqual(from_email, 'noreply@superlists')
        self.assertEqual(to_list, ['john@example.com'])

    def test_adds_success_message(self):
        response = self.client.post('/accounts/send_login_email', data={
            'email': 'john@example.com'
        }, follow=True) # pass "follow=True" to test client to tell it to get page after 302-redirect

        message = list(response.context['messages'])[0]
        self.assertEqual(
            message.message,
            "Check your email, we've sent you a link you can use to log in."
        )
        self.assertEqual(message.tags, "success")

    # check that the token created in the database is associated with email
    # from the post request
    def test_creates_token_associated_with_email(self):
        self.client.post('/accounts/send_login_email', data={
            'email': 'john@example.com'
        })
        token = Token.objects.first()
        self.assertEqual(token.email, 'john@example.com')

    # test using mocks for send_mail function, focus on 'body' argument
    # from the call arguments
    @patch('accounts.views.send_mail')
    def test_sends_link_to_login_using_token_uid(self, mock_send_mail):
        self.client.post('/accounts/send_login_email', data={
            'email': 'john@example.com'
        })

        token = Token.objects.first()
        expected_url = f'http://testserver/accounts/login?token={token.uid}'
        (subject, body, from_email, to_list), kwargs = mock_send_mail.call_args
        self.assertIn(expected_url, body)

@patch('accounts.views.auth')
class LoginViewTest(TestCase):

    def test_redirects_to_home_page(self):
        response = self.client.get('/accounts/login?token=abcd123')
        self.assertRedirects(response, '/')

    # mock auth modules in views.py
    @patch('accounts.views.auth')
    def test_calls_authenticate_with_uid_from_get_request(self, mock_auth):
        self.client.get('/accounts/login?token=abcd123')
        self.assertEqual(
            # mock out module rather than a function
            mock_auth.authenticate.call_args,
            # instead of unpacking args, use call function for neater way of calling
            call(uid='abcd123')
        )

    @patch('accounts.views.auth')
    def test_calls_auth_login_with_user_if_there_is_one(self, mock_auth):
        response = self.client.get('/accounts/login?token=abcd123')
        self.assertEqual(
            # check call args for auth.login function
            mock_auth.login.call_args,
            # check that it's called with the request object that view sees,
            # and the user object that authenticate function returns
            call(response.wsgi_request, mock_auth.authenticate.return_value)
        )

    def test_does_not_login_if_user_is_not_authenticated(self, mock_auth):
        # explicitly set return_value on auth.authenticate mock
        mock_auth.authenticate.return_value = None
        self.client.get('/accounts/login?token=abcd123')
        # assert that if authenticate returns None, shouldn't call auth.login
        self.assertEqual(mock_auth.login.called, False)