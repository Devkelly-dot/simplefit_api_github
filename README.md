# simplefit_api_github
### Fitness Without The Bells And Whistles
## About App / Usage
Simplefit is an app for keeping track of your daily lifting / cardio schedule and for counting Calories

It is not for finding advanced information on lifts, tracking calories burned while exercising, or even being a database of lifts, food, etc.  

Think of Simplefit as a glorified Notepad app with quality of life features pertaining to fitness. 

### Dayplans
Every user has 7 Dayplans (One for each day of the week) and every day plan has:
1. **Goal** - a calorie goal for that day

2. **Lifts** - a list of lifts, each with a weight, reps, and sets.
    - ie: Bench Press, 125 lb, 5 sets of 10 reps
   
3. **Cardio** - a list of cardio goals with a time or distance.
    - ie: Treadmill, 60 minutes
    
4. **Food** - a list of food, each with a name and a number of calories
    - ie: Smoothie, 200 Calories

Lifts and Cardios also have a completed attribute, which can be used during a workout to keep track of how many sets were completed and if the user was able to reach their goals.  

### Logs
Every user only has 7 Dayplans. So, they will use the Monday Dayplan to track what food they ate on Monday, but when the next Monday rolls around they will need to reset their calories, completed sets, and completed runs all back to 0 so they can track them again. (goals will remain the same, but completed sets, miles, etc will be reset).  

Users can log their Dayplans, so that they can track their progress. Logging a Day / Dayplan will create a log object with a summary of that user's calorie, lift, and cardio goals for that specific Dayplan. 

This way a user can look back on the last few days, weeks, etc and see if they have been meeting their exercise and calorie goals.   

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
 
### Endpoints
#### Dayplans
**View Dayplans** 

Used to get a list of user's 7 Dayplans (including each Dayplan's id and calorie goal) 

    Authorization Required
    
    GET dayplan/dayplans/mydayplans/

On Success, returns a list of the user (garnered from Token in header)'s Dayplans as:

    JSON {
        {
            "id":<id>,
            "user":<user>,
            "day":"SU",
            "goal":<goal>,
        },
        {
            "id":<id>,
            "user":<user>,
            "day":"MO",
            "goal":<goal>,
        },...
    }

**View Dayplan (In Detail)**

Used to view one specific dayplan and all of its lift, cardio, and food objects
    
    Authorization Required
    GET dayplan/dayplans/<int:pk>/view/

On Success returns:
    
    JSON{
        "dayplan": [{<Dayplan JSON data (seen in view Dayplans endpoint)>}],
        "food": [{<food object 1>}, {<food object 2>}, ...],
        "cardio": [{<cardio object 1>}, {<cardio object 2>}, ...],
        "lift": [{<lift object 1>}, {<lift object 2>}, ...],
    }
    

**Log Dayplan**
Used to log a specific Dayplan
 
    Authorization Required
    POST dayplan/dayplans/<int:pk>/log/

On success creates a log object of the Dayplan with id=pk and returns:

    JSON {
        "id": <id>,
        "date": "YYYY-MM-DD",
        "calories": "<complete> / <goal>",
        "lift": "<lift 1 descriptive string>, <lift 2 descriptive string>, ...",
        "cardio": "<cardio 1 descriptive string>, <cardio 2 descriptive string>, ...",
    }    

