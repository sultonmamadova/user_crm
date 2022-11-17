<!-- What will we do. Nov 12, 2022 -->
# create, read, update, delete 
read - list of users page
read - single user page
u - update the user page
d - delete the user 
create - new user
create - login
create - logout


How to start 
 python -m venv .venv - create virtual environment 
 . .venv/bin/activate - activate the environment
 pip install django - install django
 pip freeze - to see all the installation
 requirements.txt - 
 django-admin startproject config . - project started as config
 python manage.py startapp users - created users
 'users.apps.UsersConfig'- register the user in setting of the main folder (config)
 AUTH_USER_MODEL = "users.User" - +add at the end of the setting 
 class User(AbstractUser):
    pass   ----> users / models.py 
 python manage.py makemigrations - because we created new app 
 python manage.oy migrate - migrate 
 templates folder - now we can do the view and actions (for ex receive all) - where we save all the templates and django needs to know it through setting --> - TEMPLATES --> 'DIRS': BASE_DIR / "templates", now django knows it is there 
 *views -  from django.views.generic import ListView
from users.models import User
# Create your views here.
class UsersListView(ListView):
    template_name = "users/user_list.html"  -- do not mention folder template, only the folder in this folder and the file
    queryset = (
        User.objects.all("tags")
        .select_related("author")
        .filter(is_draft=False)
    )
 now *url - to add the path to find the view - 
 but for the detail view --<pk> we have to add at least one user for this we do 
 python manage.py createsuperuser
 -admin parvina, password parvina 
 next we do next the changes thro new view, not using class but function - create file forms.py in users

 cut - here we will add the stuff for the front end
All the details that we need

