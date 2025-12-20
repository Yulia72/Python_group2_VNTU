from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<name>')
def user_index(name):
    return render_template('index.html', user_name = name)

@app.route('/Articles')
def articles():
    new_articles = ['How to avoid expensive travel mistakes', 'Top 5 places to experience supernatural forces',
                    'Three wonderfully bizarre Mexican festivals', 'The 20 greenest destinations on Earth',
                    'How to survive on a desert island']
    return render_template('articles.html', articles = new_articles)

@app.route('/Admin')
def admin():
    return render_template('login_admin.html')

@app.route('/details')
def details():
    return render_template('details.html')

@app.route('/form', methods=['GET', 'POST'])
def user_form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        # Поки просто повертаємо відповідь на екран
        return f"Дякую, {name}! Ми отримали вашу форму."
    return render_template('form.html')

if __name__ == "__main__":
   app.run()

