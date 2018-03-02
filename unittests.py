import unittest
import login_mail


class LoginMailTestCase(unittest.TestCase):
    """Tests for login_mail.py"""

    def test_email_sendgrid_success(self):
        api_key = input("Enter SG API key:")
        logger = login_mail.LoggerMail(sgkey=api_key)
        response = logger.send()
        self.assertEqual(202, response.status_code, "TEST EMAIL SENDGRID SUCCES")


if __name__ == '__main__':
    unittest.main()
