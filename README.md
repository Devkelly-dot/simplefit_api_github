# simplefit_api_github
### Fitness Without The Bells And Whistles
## About App / Usage
Simplefit is an app for keeping track of your daily lifting / cardio schedule and for counting Calories

### Dayplans
Every user has 7 Dayplans (One for each day of the week) and every day plan has:
1. **Goal** - a calorie goal for that day

2. **Lifts** - a list of lifts, each with a weight, reps, and sets.
    - ie: Bench Press, 125 lb, 5 sets of 10 reps
   
3. **Cardio** - a list of cardio goals with a time or distance.
    - ie: Treadmill, 60 minutes
    
4. **Food** - a list of food, each with a name and a number of calories
    - ie: Smoothie, 200 Calories

Lifts and Cardios also have a completed attribute, which can be used during a workout to keep track of how many sets were completed. 


### Logs
Every user only has 7 Dayplans. So, they will use Monday to track what food they ate on Monday but when the next Monday rolls around they will need to reset their calories, completed sets, and completed runs all back to 0. 



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
Use the following endpoint to create an account:
    
    POST dayplan/users/register/
    JSON {
      "email":"<email>",
      "username":"<username>",
      "password":"<password>",
    }
    
When successful, this will return the user's id, email, and username. 
It will also create the User and assign them a token

To access the token / login, use the following endpoint:

    POST dayplan/users/login/
    JSON {
      "username":"<username>",
      "password":"<password>",
    }

On success, this will return:

    JSON {
       "token": "<token>"
    }

When using an endpoint with a login requirement, you must include this token in the Authorization header. 

Example using curl:
    
    curl -X GET http://localhost:8000/dayplan/dayplans/mydayplans/ -H "Authorization: Token <token>"
 
 
