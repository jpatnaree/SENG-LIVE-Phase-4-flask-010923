#!/usr/bin/env python3

# 📚 Review With Students:
    # Request-Response Cycle
    # Web Servers and WSGI/Werkzeug

# 1. ✅ Navigate to `models.py`

# 2. ✅ Set Up Imports
from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate

from models import db, Production

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)


# 3. ✅ Initialize the App
  
    
    # Configure the database
    # ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'`
    # ['SQLALCHEMY_TRACK_MODIFICATIONS'] = False` 
    

 # 4. ✅ Migrate 

# 5. ✅ Navigate to `seed.rb`

@app.before_request
def runs_before():
    current_user = {'user_id':1, 'username': "rose"}
    print(current_user)
# 6. ✅ Routes

@app.route('/')
def index():
    return (
        '<h1>Hello World</h1>'
        '<img src = https://media.npr.org/assets/img/2021/08/11/gettyimages-1279899488_wide-f3860ceb0ef19643c335cb34df3fa1de166e2761-s1100-c50.jpg />')
   
#image
@app.route('/image')
def image():
    return '<img src = https://media.npr.org/assets/img/2021/08/11/gettyimages-1279899488_wide-f3860ceb0ef19643c335cb34df3fa1de166e2761-s1100-c50.jpg />'

@app.route('/productions/<string:title>')
def production(title):
    # import ipdb; ipdb.set_trace()
    # return f'<h1>{title}</h1>'
    production = Production.query.filter(Production.title == title).first()
    propduction_response = {
        'title': production.title,
        'genre': production.genre,
        'director': production.director,
        'description': production.description,
        'image': production.image,
        'budget': production.budget,
        'ongoing': production.ongoing
    }

    response = make_response(
        jsonify(propduction_response),
        200
    )
    
    return response


# 7. ✅ Run the server with `flask run` and verify your route in the browser at `http://localhost:5000/`

# 8. ✅ Create a dynamic route



# 9.✅ Update the route to find a `production` by its `title` and send it to our browser
@app.route('/context')
def context():
    import ipdb; ipdb.set_trace()
    

# Note: If you'd like to run the application as a script instead of using `flask run`, uncomment the line below 
# and run `python app.py`

# if __name__ == '__main__':
#     app.run(port=5000, debug=True)
