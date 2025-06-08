from flask import Flask, request, jsonify
from flask_cors import CORS
import google.cloud.firestore

# --- Setup ---
app = Flask(__name__)

# --- Security Policy (The Fix) ---
# This line allows your Netlify website to make requests to this server.
CORS(app) 

# --- Database Connection ---
# =========================================================================
# PASTE YOUR GOOGLE CLOUD PROJECT ID INSIDE THE QUOTES BELOW
# =========================================================================
db = google.cloud.firestore.Client(project="mikuzzy-corporate-ventures-app") 


# --- API Routes (The Clerk's Instructions) ---

# A simple test route to check if the server is running
@app.route('/')
def index():
    return "The Mikuzzy Backend Server is running!"

# The route to add a new customer
@app.route('/add_customer', methods=['POST'])
def add_customer():
    try:
        customer_data = request.json
        # Basic check to make sure data was sent
        if not customer_data or 'name' not in customer_data:
            return jsonify({"status": "error", "message": "Missing customer name"}), 400
        
        # Save the data to the 'customers' collection in your database
        db.collection('customers').add(customer_data)
        
        print(f"Successfully added customer: {customer_data['name']}")
        return jsonify({"status": "success", "message": "Customer added successfully!"}), 201

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"status": "error", "message": "An internal server error occurred"}), 500

# You can add more routes for items, debtors, etc. here later
