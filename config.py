import os
from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
	SECRET_KEY = os.getenv('SECRET_KEY', '123456-secret')
	DEBUG = False


class DevelopmentConfig(BaseConfig):
	"""Конфигурация для стадии разработки"""
	DEBUG = True

