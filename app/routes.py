#!/usr/bin/python3
import requests
import functools
import markdown
from bs4 import BeautifulSoup
from flask import Blueprint, render_template, url_for, redirect, request, flash, get_flashed_messages
from flask_flatpages import FlatPages

main_bp = Blueprint('main', __name__)
flatpages = FlatPages()


@main_bp.app_errorhandler(404)
def handle_404(error):
	return render_template('error.html', code=404, 
							description='Страница не найдена. Попробуйте проверить URL.',
							title='404'), 404


@main_bp.app_errorhandler(401)
def handle_401(error):
	return render_template('error.html', code=401, description='Доступ запрещен. Возможно, эта страница доступна для зарегистрированных пользователей.',
							title='401'), 401


@main_bp.route('/')
def index():
	return render_template('index.html', title='Home')


@main_bp.route('/docs', methods=['GET'])
def docs():
	name = request.args.get("name", default='default')

	if name == 'default':
		return render_template('docs.html', title='Docs')
	else:
		path = '{}/{}'.format('posts', name.replace('.md', ''))
		post = flatpages.get_or_404(path)
		return render_template('doc.html', post=markdown.markdown(post.html), name=name)


@main_bp.route('/projects')
def projects():
	return render_template('projects.html', title='Projects')


@functools.lru_cache(maxsize=4096)
def get_posts():
	url = 'https://t.me/s/hex_warehouse'
	posts_list = []

	response = requests.get(url)

	if response.status_code == 200:
		soup = BeautifulSoup(response.text, 'html.parser')

		posts = soup.find_all('div', class_='tgme_widget_message_bubble')

		for post in posts:
			message = post.find('div', class_='tgme_widget_message_text')
			posts_list.append(message)

	posts_list = posts_list[1:]
	posts_list = posts_list[::-1]

	return posts_list


@main_bp.route('/contacts')
def contacts():
	return render_template('contacts.html', title='Contacts')


@main_bp.route('/gallery')
def gallery():
	return render_template('gallery.html', title='Gallery')


@main_bp.route('/posts')
def posts():
	posts_list = get_posts()

	return render_template('posts.html', title='Posts', posts=posts_list)


@functools.lru_cache(maxsize=4096)
def get_articles():
	articles_list = []
	url = 'https://habr.com/ru/users/drargentum/publications/articles'

	req = requests.get(url)

	soup = BeautifulSoup(req.text, 'html.parser')

	all_hrefs_articles = soup.find_all('a', class_='tm-title__link')

	for article in all_hrefs_articles:
		article_name = article.find('span').text
		article_link = f'https://habr.com{article.get("href")}'

		articles_list.append({
			'article_name': article_name,
			'article_link': article_link,
		})

	articles_list = articles_list[::-1]

	return articles_list


@main_bp.route('/articles')
def articles():
	articles_list = get_articles()

	return render_template('articles.html', articles=articles_list, title='Articles')
