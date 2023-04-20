from django.test import TestCase
from unittest.mock import patch
import accounts.views

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