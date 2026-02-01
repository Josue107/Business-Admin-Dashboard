from flask import request, redirect, jsonify, render_template, url_for
from flask_login import login_user, logout_user, login_required, current_user
from models import User


def register_routes(app, db, bcrypt):
    @app.route('/')
    @login_required
    def index(): 
        return render_template('index.html')

    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'POST':
            firstname = request.json.get('firstname')
            company_email = request.json.get('company_email')
            password = request.json.get('password')
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

            # Data validation can be added here

            
            user = User(firstname=firstname, company_email=company_email, password=hashed_password)
            db.session.add(user)
            db.session.commit()

            

            return redirect(url_for('login'))

        return render_template('signup.html') 

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            company_email = request.json.get('company_email')
            password = request.json.get('password')

            user = User.query.filter_by(company_email=company_email).first()
            if user and bcrypt.check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('index'))
            else:
                return jsonify({'message': 'Invalid credentials'}), 401

        return render_template('login.html')

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('login'))
