from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/contact', methods=['GET'])
def contact_us():
    return render_template('contact_us.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # You can add your code here to handle the form data, like sending an email or saving it to a database.
    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
