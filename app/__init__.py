#!/usr/bin/python3
"""Исходный код веб-приложения перепродажи автомобилей
Разработчик: Алексеев Бронислав"""
from flask import Flask
from app.routes import main_bp


def create_app():
	"""Создание приложения"""
	app = Flask(__name__)
	# Импорт конфигурации
	# + BaseConfig - базовый конфиг
	# + DevelopmentConfig - конфиг для разработки
	app.config.from_object('config.DevelopmentConfig')
	# Инициализация блюпринтов
	app.register_blueprint(main_bp)

	return app
