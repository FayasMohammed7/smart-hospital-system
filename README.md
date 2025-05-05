# Smart-hospital-system
Full-stack Hospital Web Application with graph-based indoor navigation using Dijkstra's algorithm, OTP login via Twilio, doctor appointment booking, and admin management dashboard. Built with Flask, MongoDB, and JavaScript.


🚀 Features

🔹  Graph-Based Navigation System

  Models hospital layout as a graph (adjacency list)

  Calculates the shortest path using Dijkstra’s algorithm

  Displays the path with SVG/Canvas-based animations for an interactive experience

🔹  OTP Login via Twilio

  Passwordless login system for patients using OTP sent via SMS

  Secure backend handling using Flask

🔹 Doctor Appointment Booking

  Authenticated patients can book appointments with any doctor on any available date

  All data is stored in MongoDB Atlas

🔹 Admin Panel

  Admins can view and manage all stored appointments
  

⚙️ Tech Stack

Frontend: HTML, CSS, JavaScript

Backend: Python (Flask)

Database: MongoDB (Atlas)

Authentication: Twilio OTP API

Pathfinding Algorithm: Dijkstra’s

Deployment: Docker-ready (optional)


🧪 How to Run the Application

Start the Flask backend

    python app.py
Run the frontend
Open the following files in your browser:

    index.html → Hospital navigation system

⚠️ Make sure MongoDB and Twilio credentials are configured correctly in your Flask app (app.py).

💬 Contributions & Feedback
Feel free to fork, star ⭐, and open issues or pull requests!
I'm open to feedback and collaboration on enhancing this project further.

