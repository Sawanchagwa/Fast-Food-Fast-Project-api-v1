import os

from flask import current_app

from app import app

config_name = os.getenv('APP_SETTINGS')

app = current_app(config_name)

if __name__ == '__main__':
    app.run()