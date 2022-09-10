from django.urls import path
from rest_framework.authtoken import views as rest_views

from .views import *

urlpatterns = [
    path('users/register/',CreateUserView.action), #creates 7 new dayplans for this user
    path('users/login/',rest_views.obtain_auth_token),

    ############ DAY PLANS##############
    path('dayplans/<int:pk>/log/',LogDayplanViewSet.update), # create log of day for day.id = pk
    path('logs/', MyLogViewSet.list),

    path('dayplans/mydayplans/',MyDayplansViewSet.list), #send back all of the user's dayplans
    path('dayplans/<int:pk>/clear/', DayplanClear.update), #delete all lift, cardio, and food for this day
    path('dayplans/<int:pk>/deletemodel/', DayplanDeleteModels.update),# deletes all of a model (Lift, Cardio, Food) for this dayplan
    path('dayplans/<int:pk>/clearmodel/', DayplanClearModels.update), # set all complete fields to 0 for specific model (Lift or Cardio) for this dayplan

    path('dayplans/<int:pk>/lift/',DayplanAddLift.update),

    path('dayplans/<int:pk>/cardio/',DayplanAddCardio.update),

    path('dayplans/<int:pk>/food/', DayplanAddFood.update),

    path('dayplans/<int:pk>/goal/',DayplanGoalUpdate.update), # update calories goal for the day
    path('dayplans/<int:pk>/view/',DayplanGetPlan.update_many),

    ########### LIFTS ##############
    path('lifts/<int:pk>/update/',LiftUpdate.update),
    path('lifts/<int:pk>/delete/',LiftDelete.update),

    ########## CARDIO ################
    path('cardio/<int:pk>/update/',CardioUpdate.update),
    path('cardio/<int:pk>/delete/',CardioDelete.update),


    ########## FOOD ###########
    path('food/<int:pk>/update/',FoodUpdate.update),
    path('food/<int:pk>/delete/',FoodDelete.update),
]