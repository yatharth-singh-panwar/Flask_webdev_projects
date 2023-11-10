from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

app = Flask(__name__ , template_folder='C:\\Users\\Yatharth\\OneDrive\\Desktop\\codes\\project1\\spering-html')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Areas.db'
db = SQLAlchemy(app)

class areas(db.Model):
    name = db.Column(db.String(90))
    enr_no = db.Column(db.String(90), primary_key = True)
    phone_no = db.Column(db.String(10))
    time = db.Column(db.DateTime())
    area = db.Column(db.String(100))
    vehicle = db.Column(db.String(100))

    

#defining the app routes.

@app.route('/')
def default():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/frontend.html', methods=['POST','GET'])
def frontend():
    if request.method == 'POST':
        name1 = request.form['fname']
        enro = request.form['enrol_no']
        phone = request.form['phno']
        time_str = request.form['time']
        time_obj = datetime.strptime(time_str, '%H:%M')
        area1 = request.form['adrs']
        vehicle1 = request.form.get('vehicle')

        new_person = areas(name = name1, enr_no =  enro, phone_no = phone   , time = time_obj, area =area1, vehicle =vehicle1)
        db.session.add(new_person)
        db.session.commit()

        max_time = time_obj + timedelta(minutes=30)
        area1 = request.form['adrs']  # Retrieve the area from the form

        # Query the database for records matching both conditions
        results = areas.query.filter(areas.time >= time_obj, areas.time <= max_time, areas.area == area1).all()

        return render_template('Result.html', results=results)
    
    return render_template('frontend.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
