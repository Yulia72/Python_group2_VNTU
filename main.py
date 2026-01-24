from flask import Flask
from flask import render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///side.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

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


        try:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))
        except:
            return "Помилка при реєстрації"

    return render_template('form.html')



if __name__ == "__main__":
   app.run()

