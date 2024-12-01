#!/usr/bin/python3
import sys
from app import create_app

app = create_app()


def main():
	app.run(host='0.0.0.0', port=5000)


if __name__ == '__main__':
	main()

