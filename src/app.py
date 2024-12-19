import logging
from flask import Flask, render_template
from config import Config


app = Flask(__name__,
			template_folder='templates',
			static_url_path="",
			static_folder="static")

# Set up logging configuration
logging.basicConfig(level=logging.DEBUG if Config.IS_DEBUG else logging.INFO,
					format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

# Attach the logger to the app
app.logger.setLevel(logging.DEBUG if Config.IS_DEBUG else logging.INFO)


@app.route('/')
def index():
	return render_template('index.html')


if __name__ == '__main__':
	if Config.IS_DEBUG:
		app.run(port=5000, debug=True, host='0.0.0.0')
	else:
		app.run(port=5000, debug=False, host='0.0.0.0')
