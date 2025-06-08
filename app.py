# --- The Clerk's Instruction Manual ---
from flask_cors import CORS
from flask import Flask, request, jsonify
import google.cloud.firestore

app = Flask(__name__)
CORS(app)
# IMPORTANT: Change "your-gcp-project-id" to your real Project ID inside the quotes.
db = google.cloud.firestore.Client(project="mikuzzy-corporate-app-12345")


@app.route('/add_customer', methods=['POST'])
def add_customer():
    customer_data = request.json
    db.collection('customers').add(customer_data)
    print(f"Clerk has successfully filed: {customer_data['name']}")
    return jsonify({"message": "Customer added successfully!"})

@app.route('/get_customers', methods=['GET'])
def get_customers():
    print("Clerk is going to the filing cabinet to get all files...")
    all_customers = []
    customer_files = db.collection('customers').stream()
    for file in customer_files:
        all_customers.append(file.to_dict())
    return jsonify(all_customers)