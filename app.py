from flask import Flask, request, jsonify, render_template, url_for, redirect, session
from twilio.rest import Client
from dotenv import load_dotenv
from pymongo import MongoClient
import random, time, os

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for sessions
load_dotenv()

# Twilio credentials from .env
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# MongoDB setup
local_mongo = MongoClient("mongodb://localhost:27017/")
otp_db = local_mongo["otp_auth"]

atlas_client = MongoClient("mongodb+srv://fayas:WtAyV8kWqx70BQY5@fayas.dzsqydo.mongodb.net/?retryWrites=true&w=majority&appName=fayas")
appointment_db = atlas_client['hosp']
appointment_collection = appointment_db['appointment']

# Routes

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send-otp", methods=["POST"])
def send_otp():
    phone = request.json["phone"]
    otp = str(random.randint(100000, 999999))
    client.messages.create(
        body=f"Your OTP is {otp}",
        from_=TWILIO_PHONE_NUMBER,
        to=phone
    )
    otp_db.otps.update_one({"phone": phone}, {"$set": {"otp": otp, "time": time.time()}}, upsert=True)
    return jsonify({"message": "OTP sent successfully"})

@app.route("/verify-otp", methods=["POST"])
def verify_otp():
    phone = request.json["phone"]
    otp = request.json["otp"]
    record = otp_db.otps.find_one({"phone": phone})
    if record and record["otp"] == otp:
        if time.time() - record["time"] < 300:
            session["phone"] = phone
            return jsonify({"message": "Login successful!", "redirect": url_for('appointment')})
        else:
            return jsonify({"message": "OTP expired"}), 400
    return jsonify({"message": "Invalid OTP"}), 400

@app.route("/appointment")
def appointment():
    if "phone" not in session:
        return redirect(url_for("index"))
    return render_template("appointment.html", phone=session["phone"])

@app.route("/submit", methods=["POST"])
def submit():
    if "phone" not in session:
        return redirect(url_for("index"))
    
    doctor = request.form["doctor"]
    phone = request.form["phone"]
    name = request.form["name"]
    date = request.form["date"]

    appointment = {
        "doctor": doctor,
        "phone": phone,
        "name": name,
        "date": date
    }

    appointment_collection.insert_one(appointment)
    return redirect(url_for("view_appointments"))

@app.route("/appointments")
def view_appointments():
    appointments = list(appointment_collection.find({}, {"_id": 0}))
    return render_template("view.html", appointments=appointments)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")


"""from flask import Flask, request, jsonify, render_template, url_for, redirect
from twilio.rest import Client
from dotenv import load_dotenv
from pymongo import MongoClient
import random, time, os

app = Flask(__name__)
load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

#mongo_client = MongoClient("mongodb://localhost:27017/")
#db = mongo_client["otp_auth"]

# MongoDB Atlas connection
client = MongoClient("mongodb+srv://fayas:WtAyV8kWqx70BQY5@fayas.dzsqydo.mongodb.net/?retryWrites=true&w=majority&appName=fayas")
db = client['hosp']
collection = db['appointment']

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send-otp", methods=["POST"])
def send_otp():
    phone = request.json["phone"]
    otp = str(random.randint(100000, 999999))
    message = client.messages.create(
        body=f"Your OTP is {otp}",
        from_=TWILIO_PHONE_NUMBER,
        to=phone
    )
    db.otps.update_one({"phone": phone}, {"$set": {"otp": otp, "time": time.time()}}, upsert=True)
    return jsonify({"message": "OTP sent successfully"})

@app.route("/verify-otp", methods=["POST"])
def verify_otp():
    phone = request.json["phone"]
    otp = request.json["otp"]
    record = db.otps.find_one({"phone": phone})
    if record and record["otp"] == otp:
        if time.time() - record["time"] < 300:
            return jsonify({"message": "Login successful!", "redirect": url_for('appointment')})
        else:
            return jsonify({"message": "OTP expired"}), 400
    return jsonify({"message": "Invalid OTP"}), 400

@app.route("/appointment")
def appointment():
    return render_template("appointment.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
"""