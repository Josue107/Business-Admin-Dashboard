import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Minimal config for prototyping (keep things simple)
SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret')
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'users.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
# Lower bcrypt rounds for faster dev iteration
BCRYPT_LOG_ROUNDS = int(os.environ.get('BCRYPT_LOG_ROUNDS', '4'))

# Simple role defaults
DEFAULT_ROLE = os.environ.get('DEFAULT_ROLE', 'user')
ADMIN_ROLE = os.environ.get('ADMIN_ROLE', 'admin')
