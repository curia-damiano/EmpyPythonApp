import logging

from flask import Flask, render_template

from config import Config


class App:
	""""
	Flask app instance.
	"""

	def __init__(self):
		self.flask_app = Flask(__name__, template_folder="templates", static_url_path="", static_folder="static")
		self.configure_logging()
		self.setup_routes()


	def configure_logging(self):
		logging.basicConfig(
			level=logging.DEBUG if Config.IS_DEBUG else logging.INFO,
			format="%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s",
		)
		self.flask_app.logger.setLevel(logging.DEBUG if Config.IS_DEBUG else logging.INFO)


	def setup_routes(self):
		@self.flask_app.route("/")
		def index():
			return render_template("index.html")


	def run(self):
		if Config.IS_DEBUG:
			self.flask_app.run(port=5000, debug=True, host="0.0.0.0")
		else:
			self.flask_app.run(port=5000, debug=False, host="0.0.0.0")


if __name__ == "__main__":
	app_instance = App()
	# app_instance.setup_routes()
	app_instance.run()
