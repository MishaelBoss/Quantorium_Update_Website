from flask import Flask, render_template, request, redirect, make_response, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import hashlib

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
HOST = '0.0.0.0'
PORT = 5000
server_address = '127.0.0.1:5000'
db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), nullable=False)
    intro = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text(), nullable=False)
    date = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' % self.id
    
class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.LargeBinary)
    title = db.Column(db.String(60), nullable=False)
    intro = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text(), nullable=False)
    date = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return '<Courses %r>' % self.id

@app.route('/')
@app.route('/home')
def index():
    return render_template("Index.html")

@app.route('/About')
def about():
    return render_template("About.html")

@app.route('/stepa')
def Stepa():
    return render_template("Stepa_about.html")

@app.route("/register", methods=("POST", "GET"))
def register():
    return render_template("register.html", title="Регистрация")

@app.route('/login', methods=['POST', "GET"])
def login():
        return render_template("login.html")

@app.route('/profile')
def profile():
    return render_template("profile.html")

@app.route('/Buy')
def Buy():
    return render_template("Buy.html")

@app.route('/Admin')
def admin():
    return render_template("Admin-Index.html")

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

@app.route('/login')
def Login():
    return render_template("login.html")

@app.route('/courses')
def Courses():
    return render_template("Courses.html")

@app.route('/register')
def Register():
    return render_template("Register.html")

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

        article = Article(title=title, intro=intro, text=text)

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