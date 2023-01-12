from flask import Flask, render_template

app = Flask(__name__)

#route decorator for homepage
@app.route('/')
def index():
    pizza = 'margherita'
    return render_template('index.html', pizza = pizza)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name = name)

# custom error page 
# invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# internal server error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500




