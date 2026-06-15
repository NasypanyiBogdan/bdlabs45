from flask import Flask, render_template
from controller.user_controller import user_blueprint

app = Flask(__name__)

# Реєструємо наш API контролер
app.register_blueprint(user_blueprint, url_prefix='/api')

# Роут для відображення фронтенд сайту
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    print("Flask сервер системи Ajax Systems успішно запущено!")
    app.run(debug=True, port=5000)