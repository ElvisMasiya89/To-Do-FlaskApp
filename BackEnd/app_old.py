# from flask import Flask, jsonify, request, flash, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy
# from dotenv import load_dotenv  # Import load_dotenv
# import os
# from flask_migrate import Migrate
#
# # Load environment variables from .env file
# load_dotenv()
#
# app = Flask(__name__)
#
# #Dev
# # app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')  # Get DATABASE_URI from .env
# # app.secret_key = os.getenv('SECRET_KEY')  # Get SECRET_KEY from .env
#
# #Prod
# # Read DATABASE_URI and SECRET_KEY from Docker environment variables
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
# app.secret_key = os.environ.get('SECRET_KEY')
#
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
#
#
# # Define the ToDoItem model
# class ToDoItem(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(255), nullable=False)
#     description = db.Column(db.String(1000))
#     due_date = db.Column(db.Date)
#
#
# # Route for listing all to-do items
# @app.route('/todos', methods=['GET'])
# def list_todos():
#     # Retrieve and return all to-do items from the database
#     todos = ToDoItem.query.all()
#     todo_list = [{'id': todo.id, 'title': todo.title, 'description': todo.description, 'due_date': todo.due_date} for
#                  todo in todos]
#     return jsonify(todo_list)
#
#
# from flask import Flask, jsonify, request, flash, redirect, url_for
#
#
# @app.route('/todo', methods=['POST'])
# def create_todo():
#     data = request.get_json()
#     title = data.get('title')
#     description = data.get('description')
#     due_date = data.get('due_date')
#
#     try:
#         # Create a new to-do item and save it to the database
#         new_todo = ToDoItem(title=title, description=description, due_date=due_date)
#         db.session.add(new_todo)
#         db.session.commit()
#
#         # Return a JSON response with a 200 status code for success
#         return jsonify({'message': 'To-do item created successfully'}), 200
#     except Exception as e:
#         # Handle any exceptions and return a JSON response with a 400 status code for error
#         db.session.rollback()  # Rollback the transaction in case of an error
#         return jsonify({'error': 'Error creating to-do item', 'message': str(e)}), 400
#
#
# # Main entry point for the Flask app
# if __name__ == '__main__':
#     #     # Create the database tables
#     #     db.create_all()
#     # Run the app in debug mode
#     app.run(debug=True)
