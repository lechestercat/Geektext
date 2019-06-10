from flask import Flask, render_template,redirect,make_response,request 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, validators,SubmitField 
from wtforms.validators import InputRequired,Email,Length 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:aa09@localhost/geekText"
db = SQLAlchemy(app)
migrate = Migrate(app,db)

book_copies = db.Table('book_copies',
    db.Column('user_id',db.Integer,db.ForeignKey('user.id')),
    db.Column('book_id',db.Integer,db.ForeignKey('book.id'))
)

class RegistrationForm(Form):
    username = StringField('Username',[validators.Length(min=4,max=25)])
    email    = StringField('Email address',[validators.Length(min=6,max=35)])
    password = PasswordField('New password',[
        validators.DataRequired(),
        validators.EqualTo('confirm',message="Passwords must match")
    ])
    confirm  = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS',[validators.DataRequired])
    submit  = SubmitField('Sign up')

class LoginForm(Form):
    username = StringField('username',validators=[InputRequired(),Length(min=8,max=80)])
    password = PasswordField('password',validators=[InputRequired(),Length(min=8,max=60)])
    remmember = BooleanField('remmember me')
    submit   = SubmitField('Login')


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    email = db.Column(db.String(128))
    books = db.relationship('Book',secondary=book_copies,backref=db.backref('users',lazy='dynamic'))

class Book(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    image_path = db.Column(db.String(128))
    title = db.Column(db.String(128))
    description = db.Column(db.String(128))
    price = db.Column(db.Float)



class Category(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(128))
    user_id = db.Column(db.Integer,db.ForeignKey('book.id'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template('login.html')

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html')


@app.route('/books')
def books():
    books = Book.query.all()
    print(books)

    for book in books:
        print(book.title)
        print(book.description)
        print(book.price)

    return render_template('books.html',books=books)

# book edit view 
@app.route('/book/<int:id>')
def book(id):
    book = Book.query.filter_by(id=id).first()

    return render_template('book.html',book=book)

@app.route('/user_books')
def user_books(id):

    return render_template('user_books.html')

@app.route('/user_books/<int:id>')
def user_book(id):

    return render_template('user_books.html')
@app.route('/add_to_cart')
def add_to_cart(id):

    return render_template('books.html')

@app.route('/cart')
def cart():
    # query the db for the cart object with the 
    # user id of the user of the current session

    return render_template('cart.html')

@app.route('/checkout',methods=['GET','POST'])
def checkout():
    if request.method == 'GET':
        print("het")
    else:
        pass 
    # query the db for the cart object 
    # make a new transaction class 
    # add transaction to the database 

    return render_template('checkout.html')

@app.route('/success_checkout')
def success_checkout():
    # have a flash message sent to the user that the operation 
    # was successful and a display of their transaction 
    # maybe add a pdf 

    return render_template('success_checkout')


if __name__ == '__main__':
    app.run(debug=True)

