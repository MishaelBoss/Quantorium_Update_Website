from flask import Flask, render_template, request, redirect, make_response, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
HOST = '0.0.0.0'
PORT = 5000
DEBUG = True
server_address = '127.0.0.1:5000'
db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), nullable=False)
    intro = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text(), nullable=False)
    image_data = db.Column(db.LargeBinary, nullable=False)
    date = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' % self.id
    
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    surname = db.Column(db.String(60), nullable=False, unique=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    number = db.Column(db.String(60), nullable=False)
    title = db.Column(db.String(60), nullable=False)
    text = db.Column(db.Text(), nullable=False)
    date = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return '<Feedback %r>' % self.id
    
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    title = db.Column(db.String(60), nullable=False)
    text = db.Column(db.Text(1100), nullable=False)
    date_post = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return '<Comment %r>' % self.id
    
class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    surname = db.Column(db.String(60), unique=True, nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.Text(), nullable=False)
    date = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.id


@app.route('/')
@app.route('/home')
def index():
    return render_template("Index.html")

@app.route("/register", methods=("POST", "GET"))
def register():
    if request.method == "POST":
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(name=name).first()
        if user:
            return 'Имя пользователя уже существует'

        try:
            new_user = User(name=name, surname=surname, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            return redirect('/login')
        except:
            return "Что то пошло не так"
    else:
            return render_template("register.html")

@app.route('/login', methods=['POST', "GET"])
def login():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(name=name).first()
        if user and user.password == password and user.email == email:
            session['user_id'] = user.id
            return redirect('/')
        else:
            return 'Неверный пароль или имя!'
    
    return render_template('login.html')

@app.route('/profile')
def profile():
    info = []
    try:
        info = User.query.all()
    except:
        print("Ошибка")
    return render_template('profile.html', list=info)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/')

@app.route('/Buy')
def Buy():
    return render_template("Buy.html")

@app.route('/Admin')
def admin():
    return render_template("Admin-Index.html")

@app.route('/direction_and_programs')
def Direction_and_programs():
    return render_template("direction_and_programs.html")

@app.route('/game')
def Game():
    return render_template("MyGame.html")

@app.route('/it')
def IT():
    return render_template("IT.html")

@app.route('/vr')
def VR():
    return render_template("VR.html")

@app.route('/High_tech')
def High_tech():
    return render_template("High_tech.html")


@app.route('/mathematics')
def Mathematics():
    return render_template("Mathematics.html")

@app.route('/chess')
def Chess():
    return render_template("Chess.html")

@app.route('/promrobo')
def Promrobo():
    return render_template("Promrobo.html")

@app.route('/technical_english')
def Technical_English():
    return render_template("Technical_English.html")

@app.route('/sponsor')
def Sponsor():
    return render_template("Sponsor.html")

@app.route('/profile')
def Profile():
    return render_template("Profile.html")

@app.route('/account_change')
def account_change():
    return render_template("account_change.html")

@app.route('/login')
def Login():
    return render_template("login.html")

@app.route('/courses')
def Courses():
    return render_template("Courses.html")

@app.route('/About')
def about():
    return render_template("About.html")

@app.route('/stepa')
def Stepa():
    return render_template("Stepa_about.html")

@app.route('/event')
def event():
    return render_template("event.html")

@app.route('/create_comment', methods=["POST", "GET"])
def Comments():
        if request.method == "POST":
            name = request.form['name']
            title = request.form['title']
            text = request.form['text']

            new_comment = Feedback(name=name, title=title, text=text)

            try:
                db.session.add(new_comment)
                db.session.commit()
                return redirect('/')
            except:
                return "Ошибка"
        else:
                return render_template("create_comments.html")
            

@app.route('/create_feedback', methods=["POST", "GET"])
def create_feedback():
    if request.method == "POST":
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        number = request.form['number']
        title = request.form['title']
        text = request.form['text']

        bell = Feedback(name=name, surname=surname, email=email, number=number, title=title, text=text)

        try:
            db.session.add(bell)
            db.session.commit()
            return redirect('/')
        except:
            return "Ошибка"
    else:
            return render_template("create_feedback.html")

@app.route('/bell')
def Bell():
    bell = Feedback.query.order_by(Feedback.date.desc()).all()
    return render_template("bell.html", bell=bell)

@app.route('/bell_feedback_detail/<int:id>')
def bell_feedback_detail(id):
    bell = Feedback.query.get(id)
    return render_template("bell_feedback_detail.html", bell=bell)

@app.route('/feedback/<int:id>/del')
def Feedback_delete(id):
    Bell = Feedback.query.get_or_404(id)
    try:
        db.session.delete(Bell)
        db.session.commit()
        return redirect('/bell')
    except:
        return "При удаление ароизошла ошибка"

@app.route('/products')
def products():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template("products.html", articles=articles)

@app.route('/products/<int:id>')
def products_detail(id):
    article = Article.query.get(id)
    return render_template("products_detail.html", article=article)


@app.route('/products/<int:id>/del')
def products_delete(id):
    article = Article.query.get_or_404(id)

    try:
        db.session.delete(article)
        db.session.commit()
        return redirect('/products')
    except:
        return "При удаление ароизошла ошибка"
    
@app.route('/products/<int:id>/update', methods=['POST', 'GET'])
def products_update(id):
    article = Article.query.get(id)
    if request.method == "POST":
        article.title = request.form['title']
        article.intro = request.form['intro']
        article.text = request.form['text']

        try:
            db.session.commit()
            return redirect('/products')
        except:
            return "Опа"
    else:
            return render_template("products_update.html", article=article)


@app.route('/Create-product', methods=['POST', 'GET'])
def Create_product():
    if request.method == "POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']
        image = request.files['image']

        article = Article(title=title, intro=intro, text=text, name=image.intro, image_data=image.read())

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/products')
        except:
            return "Опа"
    else:
            return render_template("Create-product.html")
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True, host=HOST, port=PORT)