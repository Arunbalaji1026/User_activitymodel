# User_activitymodel
Generated a User and their activity models , used a Custom management command i.e, a django package which monitors the user activity and designed an API to serve the data in Json format.

'''Requirement.text'''

asgiref==3.2.3
Django==3.0.6
django-filter==2.2.0
django-rest-framework==0.1.0
djangorestframework==3.11.0
pkg-resources==0.0.0
pytz==2019.3
sqlparse==0.3.0

'''Models.py''' 

created two models based on the requirement 'User and ActivityPeriod'
ActivityPeriod includes the fields required for the JSON data.

'''Views.py'''

It will import the user login and logout activities.

Queryset has been done to call the objects for the fields to be mentioned in the JSON data.


'''Initialdata.py'''

It is the command based Django Package which helps to manipulate the JSON file with dummy data's.
