from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/greet')
def greet():
    user = {'username': 'Sravya', 'age': "21"}
    return '''
<html>
    <head>
        <title>Templating</title>
    </head>
    <body>
        <h1>Hello, ''' \
            + user['username'] \
            + '''! You will turn to ''' \
            + user['age'] + ''' on May 15th.</h1>
    </body>
</html>'''


@app.route('/hello')
def hello():
    return render_template('index.html', name="Sravya")


@app.route('/form', methods=['POST', 'GET'])
def bio_data_form():
    if request.method == "POST":
        username = request.form['username']
        age = request.form['age']
        email = request.form['email']
        hobbies = request.form['hobbies']
        return redirect(url_for('showbio',
                                username=username,
                                age=age,
                                email=email,
                                hobbies=hobbies))
    return render_template("bio_form.html")


@app.route('/showbio', methods=['GET'])
def showbio():
    username = request.args.get('username')
    age = request.args.get('age')
    email = request.args.get('email')
    hobbies = request.args.get('hobbies')
    return render_template("show_bio.html",
                           username=username,
                           age=age,
                           email=email,
                           hobbies=hobbies)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
