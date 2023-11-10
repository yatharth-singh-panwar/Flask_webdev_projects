from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Contact.db'
db = SQLAlchemy(app)

class Contact(db.Model):
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False, primary_key=True)
    message = db.Column(db.Text, nullable=False)

# Defining routes for each page
@app.route('/')
def default():
    return render_template('index.html')


@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/proteins.html')
def proteins():
    return render_template('proteins.html')

@app.route('/fats.html') 
def fats():
    return render_template('fats.html')

@app.route('/carbohydrates.html')
def carbohydrates():
    return render_template('carbohydrates.html')

@app.route('/vitaminsminerals.html')
def vitaminsminerals():
    return render_template('vitaminsminerals.html')

@app.route('/team.html')
def team():
    return render_template('team.html')

@app.route('/blog.html')
def blog():
    return render_template('blog.html')

@app.route('/bmr calc.html')
def bmr_calc():
    return render_template('bmr calc.html')

@app.route('/BMI.html')
def bmi():
    return render_template('BMI.html')

@app.route('/contact_us.html', methods=['GET','POST'])
def contact_us():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        new_contact = Contact(name=name, email=email, message=message)
        db.session.add(new_contact)
        db.session.commit()
        return "Thankyou your message has been sent. : )"

    return render_template('contact_us.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
