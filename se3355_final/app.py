from flask import Flask, render_template, request, flash, redirect, url_for, request,abort,Blueprint,session
from werkzeug.security import generate_password_hash, check_password_hash
from model import db,Hotel,User
from datetime import datetime, timedelta



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://berk2k:Admin1239@berk2k.mysql.pythonanywhere-services.com/berk2k$berk2k_se3355_final' #'mysql://root:berkberk09@localhost:3306/se3355_final'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure secret key
db.init_app(app)

'''
with app.app_context():
    db.create_all()

hotels = [
    Hotel(description="Nex Hotel Istanbul City Center",location="Istanbul", price=6200.0, image_url="img1.jpg",num_of_comments=10,rating=10.0,member = 1,availability=1),
    Hotel(description="Cassa Nonna Bodrum",location="Bodrum", price=13000.0, image_url="img2.jpg",num_of_comments=8,rating=7.7,member = 1,availability=1),
    Hotel(description="Sundia Exclusive By Liberty Fethiye",location="Fethiye", price=9000.0, image_url="img3.jpg",num_of_comments=5,rating=9.0,member = 0,availability=0),

]


users = [
    User(first_name="Berk",last_name="Polat",email="test@gmail.com",password="12345",country="Turkiye",city="Izmır")
]
with app.app_context():
    for user in users:
        db.session.add(user)

    db.session.commit()
'''

@app.route('/')
def home():
    today = datetime.now()
    days_until_sunday = (6 - today.weekday() + 1) % 7
    weekend_date = today + timedelta(days=days_until_sunday)

    
    available_hotels = Hotel.query.filter_by(availability=1).all()
    sorted_results = sorted(available_hotels, key=lambda hotel: hotel.rating, reverse=True)
    user_id = session.get("user_id")

    user = User.query.get(user_id)

    return render_template('home.html', weekend_date=weekend_date, available_hotels=sorted_results,user = user)
    

auth_blueprint = Blueprint('auth', __name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":

        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email,password=password).first()

        if user:
            
            session['user_id'] = user.id
            return redirect(url_for('home'))
        else:
            return render_template('login.html')
    return render_template('login.html')

@app.route('/logout')
def logout():
    
    session.clear()
    return redirect(url_for('home'))
    

@app.route('/register', methods=['GET', 'POST'])
def register():
    
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        country = request.form['country']
        city = request.form['city']

        
        if password != confirm_password:
            return redirect(url_for('login'))

        
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return redirect(url_for('register'))

        
        new_user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            country=country,
            city=city
        )
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))
    
    return render_template('register.html')

    
    

@app.route('/search', methods=['GET'])
def search():
    arrival = request.args.get('arrival')
    date = request.args.get('date')
    guests = request.args.get('guests')
    
    if arrival and date:
        search_results = Hotel.query.filter(Hotel.location.ilike(f'%{arrival}%'))
        date_obj = datetime.strptime(date, '%Y-%m-%d')

    
        if date_obj.weekday() in {5,6}:  # Cuma günü
            search_results = [hotel for hotel in search_results if hotel.availability]
            search_results = [hotel for hotel in search_results if hotel.location.lower() == arrival.lower()]
    else:
        search_results = Hotel.query.all()
    
    

        

    return render_template('search.html', search_results=search_results)

@app.route('/details/<int:id>')
def details(id):
    hotel = Hotel.query.get(id)
    
    if hotel is None:
        abort(404)  

    return render_template('details.html', hotel=hotel)



if __name__ == '__main__':
    app.run(debug=True)
