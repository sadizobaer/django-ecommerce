Commands
# for creating virtual environment
1. python3 -m venv env
# for install django
2. pip install django
# creating project in django
3. django-admin startproject ecommerce
# to run the server 
4. ./manage.py runserver
# to get all packages togather
5. pip freeze requirements.txt 
# to manage environment files also need to install wheel first
6. pip install wheel and then pip install django-dotenv
# to install drf
7. pip install djangorestframework
# for testing
8. pip install pytest && pip install pytest-django
# for adding app on project
9. ./manage.py startapp product
# tp work with trees of model instances
10. pip install django-mptt