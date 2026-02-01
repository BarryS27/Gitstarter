from flask_frozen import Freezer
from app import app

app.config['FREEZER_BASE_URL'] = '/Gitstarter/'

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()