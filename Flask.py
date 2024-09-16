from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = 'your secret key'

def init_db():
    conn = sqlite3.connect('shoping.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        name TEXT UNIQUE,
        email TEXT UNIQUE,
        bio TEXT UNIQUE
    )''')

    conn.execute('''CREATE TABLE IF NOT EXISTS cart_items(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        item TEXT,
        quantity INTEGER,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )''')
    conn.close()

init_db()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        try:
            conn = sqlite3.connect('shoping.db')
            conn.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password))
            conn.commit()
            conn.close()
            return redirect(url_for('home'))
        except sqlite3.IntegrityError:
            return "Username or email already exists"

    return render_template('signup.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = sqlite3.connect('shoping.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            session['user_id'] = user[0]
            session['username'] = user[1]
            return redirect(url_for('account'))
        else:
            return "Invalid credentials"
    
    return render_template('login.html')

@app.route('/account/')
def account():
    if 'username' in session:
        return render_template('account.html', username=session['username'])
    else:
        return redirect(url_for('login'))

# Cart management with database
@app.route('/appliances/')
def appliances():
    return render_template('appliances.html')

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    if 'user_id' in session:
        item = request.form.get('item')
        user_id = session['user_id']

        # Insert item into cart_items table in the database
        conn = sqlite3.connect('shoping.db')
        conn.execute('INSERT INTO cart_items (user_id, item, quantity) VALUES (?, ?, ?)', (user_id, item, 1))
        conn.commit()
        conn.close()
        return redirect(url_for('cart'))
    else:
        return redirect(url_for('login'))

@app.route('/cart/')
def cart():
    if 'user_id' in session:
        user_id = session['user_id']

        # Fetch items from the cart_items table for the logged-in user
        conn = sqlite3.connect('shoping.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, item, quantity FROM cart_items WHERE user_id = ?', (user_id,))
        cart_items = cursor.fetchall()
        conn.close()

        return render_template('cart.html', cart_items=cart_items)
    else:
        return redirect(url_for('login'))

@app.route('/remove_from_cart/<int:item_id>')
def remove_from_cart(item_id):
    if 'user_id' in session:
        conn = sqlite3.connect('shoping.db')
        conn.execute('DELETE FROM cart_items WHERE id = ?', (item_id,))
        conn.commit()
        conn.close()

        return redirect(url_for('cart'))
    else:
        return redirect(url_for('login'))

# Other routes
@app.route('/category/')
def category():
    return render_template('category.html')

@app.route('/help/')
def help():
    return render_template('help.html')

@app.route('/order/')
def order():
    return render_template('order.html')

@app.route('/sell/')
def sell():
    return render_template('sell.html')

@app.route('/legal/')
def legal():
    return render_template('legal.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/services/')
def services():
    return render_template('services.html')

@app.route('/electronic/')
def electronic():
    return render_template('electronic.html')

@app.route('/fassion/')
def fassion():
    return render_template('fassion.html')

@app.route('/mobile/')
def mobile():
    return render_template('mobile.html')

@app.route('/home_decor/')
def home_decor():
    return render_template('home_decor.html')

@app.route('/personal/')
def personal():
    return render_template('personal.html')

@app.route('/buy/')
def buy():
    return render_template('buy.html')

if __name__ == '__main__':
    app.run(debug=True)