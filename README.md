# simplefit_api_github
### Manage Lifts, Cardio, and Calories with no extra headache
## Installation
1. Clone this rep
2. Create virtual environment using Python 3.10.4
3. Run pip install -r requirements.txt
4. Run Python manage.py runserver 8000
5. Access on localhost:8000
## Documentation
### Create Admin
1. Run python manage.py createsuperuser
2. Access admin panel on localhost:8000/admin/
### Token Authentication 
This app uses token authentification, so every user is assigned a token when their account is created. 
To access sensitive information or perform POST actions that affect a user's account, the user's token must be included in the Header
#### Registration
To Register a new account, which creates a user and assigns them a Token, use the following endpoint: 
  
  POST /users/register/
