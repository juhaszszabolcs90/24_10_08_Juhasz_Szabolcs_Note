from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def index():
    product_name = None
    if request.method == 'POST':
        product_name = request.form['product_name']
    return render_template('index.html', product=product_name)


if __name__ == "__main__":
    app.run(debug=True)