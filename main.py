from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/login', methods=["POST", "GET"])
def login_response_page():
    password = request.form['password']
    username = request.form['username']
    print(type(request))
    print(request.data)
    print(password)
    return render_template('login_response.html', name=username, password=password)


if __name__ == "__main__":
    app.run(debug=True)
