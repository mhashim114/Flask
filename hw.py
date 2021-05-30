# Python Imports
from flask import Flask, render_template, request, url_for, redirect, session, g
import model, logging

# Local Imports
from controllers.parsing import parse 

app = Flask(__name__)

app.secret_key = 'jumpingjacks'

username = ''
user = model.check_user()

@app.route('/', methods =['GET'])
def home_page():
    if 'username' in session:
        g.user = session['username']
        return render_template('football.html', message = 'login Successful')
    return render_template('homepage.html', message = 'Login or Signup!!!')


@app.route('/login', methods = ['GET', 'POST'])
#@parse
def login():
    if request.method == 'POST':
        session.pop('username', None)
        username = request.form['username']
        pwd = request.form['password']
        if model.user_exists(username, pwd):
            app.logger.info("USER EXISTS")
            session['username'] = request.form['username']
            return redirect(url_for('home_page'))
            
    return render_template('index.html')

@app.before_request
def before_request():
    g.username = None
    if 'username' in session:
        g.username = session['username'] 

@app.route('/getsession')
def getsession():
    if 'username' in session:
        return session['username']
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home_page')) 


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

@app.route('/login1', methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        username = request.form['username']
        password = request.form['password']

        if model.user_exists(username, password):
            success_message = 'Login Successful'
            return redirect(url_for('dashboard'))
        else:
            error_message = 'Invalid credentials'
            return render_template('index.html', message = error_message)
         
@app.route('/dashboard', methods = ['GET', 'POST'])
def dashboard():
    if request.method == 'GET':
        lists = model.show_all_lists()
        return render_template('dashboard.html', lists = lists)
    else:
        lists = model.show_all_lists()
        if 'show_items' in request.form:
            todo_list = request.form['lists']
            list_items = model.show_all_list_items(todo_list)
            return render_template('dashboard.html', lists = lists, list_items = list_items)
        
        if 'update_item' in request.form:
            lists = model.show_all_lists()
            todo_list = request.form['lists']
            list_items = request.form['item']
            model.update_item(todo_list, list_items)
            return render_template('dashboard.html', lists = lists, list_items = list_items)

@app.route('/create_new_list', methods = ['POST'])
def new_list():
    newList = request.form['new_list']
    message = model.create_new_list(newList)
    
    app.logger.info(message)
    return redirect(url_for('dashboard'))

@app.route('/add_item', methods = ['POST'])
def add():
    newItem = request.form['new_item']
    inList = request.form['lists']
    message = model.add_item_in_list(newItem, inList)
    
    app.logger.info(message)
    return redirect(url_for('dashboard'))

@app.route('/update_item', methods = ['POST'])
def update_item():
    item = request.form['item']
    if item:
        model.update_item(item)


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

