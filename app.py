from flask import Flask, request, jsonify
from flask_cors import CORS
import google.cloud.firestore

app = Flask(__name__)
CORS(app) 

# --- IMPORTANT ---
# MAKE SURE YOUR CORRECT PROJECT ID IS IN THE QUOTES BELOW
db = google.cloud.firestore.Client(project="mikuzzy-corporate-ventures-app") 

# Test route to see if the server is running
@app.route('/')
def index():
    return "The Mikuzzy Backend Server is running!"

# Route to ADD a new customer
@app.route('/add_customer', methods=['POST'])
def add_customer():
    try:
        customer_data = request.json
        db.collection('customers').add(customer_data)
        return jsonify({"status": "success", "message": "Customer added."}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Route to GET all existing customers
@app.route('/get_customers', methods=['GET'])
def get_customers():
    try:
        all_customers = []
        docs = db.collection('customers').stream()
        for doc in docs:
            customer_data = doc.to_dict()
            customer_data['id'] = doc.id
            all_customers.append(customer_data)
        return jsonify(all_customers), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
