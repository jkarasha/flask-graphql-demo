import os

class Config(object):
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
  SQLALCHEMY_DATABASE_URI = "sqlite:///graphql-demo.db"
  DB_USER = os.environ.get('DB_USER')
  DB_PASSWORD = os.environ.get('DB_PASSWORD')
  DB_HOST = os.environ.get('DB_HOST') or 'localhost'
  DB_HOST_PORT = os.environ.get('DB_HOST_PORT') or '5432'
  DB_NAME = os.environ.get('DB_NAME') or 'graphql-demo'
  #postgresql://<username>:<password>@<server>:5432/<db_name>
  #SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_HOST_PORT}/{DB_NAME}"
  #SQLALCHEMY_DATABASE_URI = "postgresql://postgres:{P@ssw0rd2021!@}@localhost:5432/graphql-demo"
  SQLALCHEMY_TRACK_MODIFICATIONS = False
