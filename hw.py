from flask import Flask, render_template, request, flash
import model

app = Flask(__name__)

@app.route('/', methods =['GET'])
def home_page():
    return render_template('home.html')

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        username = request.form['username']
        password = request.form['password']

        if model.user_exists(username):
            error_message = 'Username already exists'
            return render_template('signup.html', message = error_message)
        
        message = model.create_account(username, password)
        return render_template('signup.html', message = message)

@app.route('/login', methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        username = request.form['username']
        password = request.form['password']

        if model.user_exists(username, password):
            success_message = 'Login Successful'
            return render_template('dashboard.html')
        else:
            error_message = 'Invalid credentials'
            return render_template('index.html', message = error_message)
         
@app.route('/dashboard', methods = ['GET'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/about', methods = ['GET'])
def about():
    return render_template('about.html')


@app.route('/terms', methods = ['GET'])
def terms_of_use():
    return render_template('terms.html')

@app.route('/privacy', methods = ['GET'])
def privacy():
    return render_template('privacy.html')

@app.route('/showPass', methods = ['GET', 'POST'])
def admin_pass():
    if request.method == 'GET':
        return render_template('football.html')
    else:
        username = request.form['username']
        password = model.show_admin_pass(username)
        return render_template('football.html', message = password)





if __name__ == '__main__':
    app.run(debug = True, port = 8000)

