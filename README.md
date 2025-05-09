M-Pesa Prompt Integration


This repository contains a Django-based application that integrates with the M-Pesa API to initiate payment prompts. It demonstrates how to send payment requests to users via M-Pesa's STK Push service.

Features
STK Push Integration: Initiates payment prompts to users' mobile devices using M-Pesa's STK Push API.

Django Framework: Utilizes Django for rapid web development and clean design.

SQLite Database: Stores transaction records using a lightweight SQLite database.

Project Structure
mpesademo/: Contains the main Django project settings and configurations.

myapp/: Django application handling the core logic for M-Pesa integration.

db.sqlite3: SQLite database file storing transaction data.

manage.py: Django's command-line utility for administrative tasks.

.env: Environment variables file (ensure this file is excluded from version control for security).

Technologies Used
Python: Programming language used for development.

Django: High-level Python web framework.

SQLite: Lightweight database for development and testing.

Getting Started
Prerequisites
Python 3.x installed on your machine.

Virtual environment tool (optional but recommended).

Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/Arthur-Muriuki/mpesa-prompt.git
cd mpesa-prompt
Create and activate a virtual environment (optional):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Configure environment variables:

Create a .env file in the root directory and add the necessary M-Pesa API credentials:

env
Copy
Edit
CONSUMER_KEY=your_consumer_key
CONSUMER_SECRET=your_consumer_secret
SHORTCODE=your_shortcode
PASSKEY=your_passkey
Apply migrations:

bash
Copy
Edit
python manage.py migrate
Run the development server:

bash
Copy
Edit
python manage.py runserver
Access the application:

Open your browser and navigate to http://localhost:8000.

Usage
Navigate to the application's homepage.

Enter the required payment details.

Submit the form to initiate an M-Pesa STK Push to the provided phone number.

Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.
