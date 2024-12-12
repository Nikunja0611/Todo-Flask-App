from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost/todo"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Create a Todo model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)

# Route for the home page
@app.route('/')
def home():
    todos = Todo.query.all()  # Fetch all todos from the database
    return render_template("index.html", todos=todos)

# Route to add a new todo
@app.route('/add', methods=['POST'])
def add_todo():
    title = request.form['title']
    description = request.form['description']
    new_todo = Todo(title=title, description=description)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('home'))

# Route to delete a todo
@app.route('/delete/<int:id>')
def delete_todo(id):
    todo_to_delete = Todo.query.get_or_404(id)
    db.session.delete(todo_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    # Create database tables (uncomment for the first run)
    with app.app_context():
        db.create_all()
    app.run(debug=True)
