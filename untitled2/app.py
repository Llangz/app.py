from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    data = (1, 'John Doe', 'jd@yahoo.com', 'Male')
    return render_template('home.html', person=data)

@app.route('/about')
def about():
    cars = ['Toyota', 'Honda', 'Mercedes', 'Range Rover', 'Mitsubishi']
    user = 'John Mark'
    date = '10-9-2000'
    return render_template('about.html', cars=cars, user=user, date=date)


@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/products/<id>')
def products(id):
    return 'you are on product number '+id

@app.route('/items/<id>/<user>')
def items(id, user):
    return 'you are on item {} and you are user {}'.format(id, user)

@app.errorhandler(404)
def error(x):
    return 'Hey,that page seems not be there'


if __name__ == '__main__':
    app.run(debug=True, port=8000)


