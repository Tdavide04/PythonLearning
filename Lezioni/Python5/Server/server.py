from flask import Flask, request, render_template

api = Flask("__name__")


@api.route('/')
def index():
    return render_template("index.html")

@api.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    surname = request.form.get('surname')
    return render_template('index2.html', name=name, surname=surname)

if __name__ == '__main__':
    api.run(debug=True)

api.run(host="0.0.0.0", port=8085)
