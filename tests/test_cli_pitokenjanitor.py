import unittest
from flask.testing import CliRunner
from privacyidea.cli import pi_token_janitor


class PITokenJanitorLoadTestCase(unittest.TestCase):
    def test_01_pitokenjanitor_help(self):
        runner = CliRunner()
        result = runner.invoke(pi_token_janitor, ["-h"])
        self.assertIn("Loads token data from a PSKC file.",
                      result.output, result)
        self.assertIn("This can update existing tokens in the privacyIDEA system.",
                      result.output, result)
        self.assertIn("Finds all tokens which match the conditions.",
                      result.output, result)
