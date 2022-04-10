# configurations to connect to sqlite db

db_name = 'db/course.db'

db_URI = "sqlite:///" + db_name

class Config(object):
    SQLALCHEMY_DATABASE_URI = db_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = True