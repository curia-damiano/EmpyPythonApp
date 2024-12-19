import os
from dotenv import load_dotenv


class Config:
	"""
	Configuration class for this application.
	"""

	load_dotenv()

	APP_ENV = os.getenv("APP_ENV", "production")  # Defaults to "production" if not set
	IS_DEBUG = APP_ENV.lower() == "development"
	print(f"The app starts in {APP_ENV} mode, DEBUG={IS_DEBUG}")


if Config.APP_ENV not in ('production', 'development'):
	raise ValueError("APP_ENV must be either 'production' or 'development'")
