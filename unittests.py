import unittest
from bin import Logger


class LoginMailTestCase(unittest.TestCase):
    """Tests for bin.Logger.LoggerMail"""

    def test_email_sendgrid_success(self):
        logger = Logger.Logger().get_logger("SG")
        response = logger.send(test=True)
        self.assertEqual(202, response.status_code, "TEST EMAIL SENDGRID SUCCES")


if __name__ == '__main__':
    unittest.main()
