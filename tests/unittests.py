import unittest
from bin import Loggers


class LoggersTestCase(unittest.TestCase):
    """Tests for bin.Loggers.LoggerMail"""
    def setUp(self):
        print("\n=== INITIALIZING TESTS FOR LOGGERS ===")
        self.loggers = Loggers.logger_factory

    def test_email_sendgrid_success(self):
        logger = self.loggers("SG")
        response = logger.log(test=True)
        self.assertEqual(202, response.status_code, "TEST EMAIL SENDGRID FAILED")

    def tearDown(self):
        print("=== FINISHED TESTS FOR LOGGERS ===")


if __name__ == '__main__':
    unittest.main()
