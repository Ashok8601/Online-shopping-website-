# Flask Shopping App

This Flask application allows users to sign up, log in, and access different categories of products. It uses an SQLite database to manage user accounts and includes various routes for product categories, help, and account management.

## Features
- User Signup and Login with SQLite Database
- Account page that displays user information (username, email)
- Product category pages for easy browsing
- Additional pages for cart, orders, selling, legal, contact, and services

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/shoping-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd shoping-app
    ```

3. Install required dependencies using pip:

    ```bash
    pip install flask
    ```

4. Create the SQLite database and initialize it:

    The `init_db()` function creates the required `users` table in the `shoping.db` file. This table stores information about users such as their username, password, and email.

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open a web browser and navigate to:

    ```
    http://127.0.0.1:5000
    ```

3. Use the signup page to create an account, then log in with your credentials.

## Database Structure

The SQLite database stores user information in a `users` table with the following columns:

- `id`: Auto-incrementing user ID
- `username`: Unique username for each user
- `password`: User password
- `email`: User email address
- `reel`, `post`, `name`, `bio`, `follower`, `following`, `dob`: Additional fields for user profile information

## Routes

- `/` - Home page
- `/signup/` - User Signup page
- `/login/` - User Login page
- `/account/` - Account page, displaying logged-in user's information
- `/category/` - Product categories page
- `/cart/` - User shopping cart page
- `/order/` - Order history page
- `/sell/` - Sell your products page
- `/legal/` - Legal information page
- `/contact/` - Contact information page
- `/services/` - List of services page
- `/appliances/`, `/electronic/`, `/fassion/`, `/mobile/`, `/home_decor/`, `/personal/`, `/buy/` - Category-specific product pages

## Templates

The app uses the `render_template()` function to serve HTML templates for each route. Ensure that you have the following HTML files in your `templates/` directory:
- `home.html`
- `signup.html`
- `login.html`
- `account.html`
- `category.html`
- `help.html`
- `cart.html`
- `order.html`
- `sell.html`
- `legal.html`
- `contact.html`
- `services.html`
- `appliances.html`
- `electronic.html`
- `fassion.html`
- `mobile.html`
- `home_decor.html`
- `personal.html`
- `buy.html`

## License

This project is open source and available under the [MIT License](LICENSE).
