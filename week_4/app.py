from flask import Flask, request
from flask_restful import Api, Resource
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required
)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask app
app = Flask(__name__)
api = Api(app)

# Configure the JWT secret key
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
jwt = JWTManager(app)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))

# Create database tables
with app.app_context():
    db.create_all()

# User Registration
class Register(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        if User.query.filter_by(username=username).first():
            return {"message": "User already exists"}, 400
        
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return {"message": "User registered successfully"}, 201

# User Login
class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if not user or not check_password_hash(user.password, password):
            return {"message": "Invalid credentials"}, 401
        
        access_token = create_access_token(identity=username)
        return {"access_token": access_token}, 200

# CRUD Operations for Items
class ItemResource(Resource):
    # Read an item by id
    @jwt_required()
    def get(self, item_id):
        item = Item.query.get(item_id)
        if item:
            return {"id": item.id, "name": item.name, "description": item.description}, 200
        return {"message": "Item not found"}, 404

    # Create a new item
    @jwt_required()
    def post(self):
        data = request.get_json()

        # Validate that 'name' is present
        if 'name' not in data or not data['name']:
            return {"message": "Item 'name' is required"}, 400
        
        new_item = Item(name=data['name'], description=data.get('description', ''))
        db.session.add(new_item)
        db.session.commit()
        return {"message": "Item created", "item": {"id": new_item.id, "name": new_item.name}}, 201

    # Update an existing item
    @jwt_required()
    def put(self, item_id):
        data = request.get_json()
        item = Item.query.get(item_id)

        if not item:
            return {"message": "Item not found"}, 404
        
        item.name = data.get('name', item.name)
        item.description = data.get('description', item.description)
        db.session.commit()
        
        return {"message": "Item updated", "item": {"id": item.id, "name": item.name}}, 200

    # Delete an item
    @jwt_required()
    def delete(self, item_id):
        item = Item.query.get(item_id)
        if not item:
            return {"message": "Item not found"}, 404
        
        db.session.delete(item)
        db.session.commit()
        return {"message": "Item deleted"}, 200

# Add routes
api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(ItemResource, '/item/<int:item_id>', '/item')

if __name__ == '__main__':
    app.run(debug=True)
