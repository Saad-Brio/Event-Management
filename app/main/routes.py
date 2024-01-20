from flask import Blueprint, render_template
from db.admin_operations import AdminOperations

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@main.route('/create/admin', methods=['POST'])
def create_admin():
    AdminOperations.create_admin('Jhon Doe', 'jhon_doe', 'jhon@example.com', 'password123')
    return 'Admin create successfully'
