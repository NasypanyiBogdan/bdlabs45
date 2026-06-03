from flask import Flask
from domain import db
from controller import movie_bp

app = Flask(__name__)

# Налаштування підключення до MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:$$44pilotsua@localhost/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Реєструємо контролер
app.register_blueprint(movie_bp)

if __name__ == '__main__':
    app.run(debug=True)