from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

products = []
users = []

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/submit_products', methods = ['POST'])
def submit_products():
    product_name = request.form.get('product_name')
    if product_name:
        products.append(product_name)
    return redirect(url_for('index'))

@app.route('/products')
def get_products():
    return render_template('products.html', products=products)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Itt összegyűjtjük az űrlap adatait
        user_data = {
            'fullname': request.form.get('fullname'),
            'email': request.form.get('email'),
            'password': request.form.get('password'),
            'phone': request.form.get('phone'),
            'birthdate': request.form.get('birthdate'),
            'gender': request.form.get('gender'),
            'interest': request.form.get('interest'),
            'color': request.form.get('color'),
            'fav_time': request.form.get('fav-time')
        }
        # Adatok hozzáadása a users listához
        users.append(user_data)
        return redirect(url_for('admin'))
    return render_template('signup_form.html')

@app.route('/admin')
def admin():
    return render_template('admin.html', users=users)

if __name__ == "__main__":
    app.run(debug=True)