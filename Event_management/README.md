EVENT_MANAGEMENT    
Prerequisites
Before running the project, make sure you have the following installed:

Python 3.8 or later
pip (Python package installer)


Installation

1. Clone the Repository
bash
Copy code
git clone https://github.com/Rajat44153/Event_management.git
cd event-management-api

2. Create a Virtual Environment
bash
Copy code
python3 -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows

3. Install the Dependencies
bash
Copy code
pip install -r requirements.txt

4. Set Up the Database
Run migrations to set up the database:

bash
Copy code
python manage.py migrate

5. Create a Superuser for Admin Access
bash
Copy code
python manage.py createsuperuser
Follow the prompts to create an admin user.

6. Run the Development Server
bash
Copy code
python manage.py runserver
The application will be available at http://127.0.0.1:8000.


Authentication
POST /api/auth/login: Authenticates users (Admin or User) and returns a JWT token.
Request Body:
json
Copy code
{
  "username": "admin",
  "password": "yourpassword"
}
Response:
json
Copy code
{
  "token": "your-jwt-token-here"
}

Authentication & Authorization
JWT Token: All requests to the API requiring authentication must include a valid JWT token in the Authorization header.

Example:

bash
Copy code
curl -H "Authorization: Bearer <your-jwt-token>" http://127.0.0.1:8000/api/events/
Admin Role: Admins have full access to create, update, and delete events.

User Role: Users can only view events and purchase tickets.

Example Usage
1. Login as an Admin
bash
Copy code
curl -X POST http://127.0.0.1:8000/api/auth/login -d '{"username": "admin", "password": "adminpassword"}' -H "Content-Type: application/json"
2. Create an Event (Admin Only)
bash
Copy code
curl -X POST http://127.0.0.1:8000/api/events/ -d '{
  "title": "Art Exhibition",
  "description": "A beautiful art exhibition showcasing modern art.",
  "date": "2024-12-10T10:00:00",
  "location": "New York",
  "ticket_price": 40
}' -H "Authorization: Bearer <admin-jwt-token>" -H "Content-Type: application/json"
3. Purchase Tickets (User Only)
bash
Copy code
curl -X POST http://127.0.0.1:8000/api/tickets/purchase/ -d '{
  "event_id": 1,
  "quantity": 3
}' -H "Authorization: Bearer <user-jwt-token>" -H "Content-Type: application/json"# Event_management