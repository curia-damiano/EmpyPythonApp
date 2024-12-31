import unittest

from src.app import App


class FlaskAppTests(unittest.TestCase):
	"""
	Unit tests for the Flask application.

	This class contains tests for the Flask application, including tests for the index route
	and logging setup. It uses the unittest framework to set up a test client and verify
	the application's behavior.

	Methods:
		setUp():  Sets up the test client for the Flask application.
		test_*(): Various test methods to test the application's behavior.
	"""

	def setUp(self):
		# Set up the test client
		flask_app = App().flask_app
		self.app = flask_app.test_client()
		self.app.testing = True
		self.logger = flask_app.logger


	def test_index(self):
		# Test the index route
		response = self.app.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertIn(b'<!DOCTYPE html>', response.data)


	def test_logging(self):
		# Test if logging is set up correctly
		with self.assertLogs(self.logger, level='INFO') as log:
			self.logger.info('Testing logging')
			self.assertIn('INFO:src.app:Testing logging', log.output)


if __name__ == '__main__':
	unittest.main()
