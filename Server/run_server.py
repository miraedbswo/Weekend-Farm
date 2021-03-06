import os

from app import create_app
from config.config import Config


if __name__ == '__main__':
    app = create_app(Config)

    if 'SECRET_KEY' not in os.environ:
        print('[WARN] SECRET KEY is not set in the environment variable !!')

    app.run(**app.config['RUN_SETTINGS'])
