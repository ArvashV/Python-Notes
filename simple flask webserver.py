from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask Web Server!"

@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name}!"

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        return f"Hello, {name}!"
    return '''
        <form method="post">
            Name: <input type="text" name="name"><br>
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
