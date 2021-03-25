from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == 'admin':
            success_message = 'Login Successful'
            return render_template('index.html', message = success_message)
        else:
            error_message = 'Invalid credentials'
            return render_template('index.html', message = error_message)

@app.route('/football', methods = ['GET'])
def football():
    return render_template('football.html') 

@app.route('/about', methods = ['GET'])
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug = True, port = 8000)

