# Nathan Yee
# 1 Sep 2020

# Goal:
# to create an inventory management system for IT services

# Features:
# Search, find, display available systems (monitors, computers, keyboard, mouse) that are ready for deployment
# add inventory using forms created in Python

# Languages:
# Python, SQL, html, css

## removed from line 13 on index.html
<a href="{% url 'display_mobiles' %}" class="btn btn-primary btn-md" role="button">Mobiles</a>
<a href="{% url 'add_mobile' %}" class="btn btn-primary btn-md" role="button">+</a>
# Reason: Do no

# runserver command
# python manage.py runserver 192.168.0.231:8000


Notes
################################################################################
# django commands


# How to start Django local server
1. Go to directory with manage.py inside
2. run -> python manage.py runserver
3. enter address created in cmd into web browser

# How to create admin account for django local server
1. Go to directory with manage.py inside
2. run -> python manage.py createsuperuser
3. input account info

# How to add value to the sql database
1. Change your models (in models.py).
2. Run python manage.py makemigrations to create migrations for those changes
3. Run python manage.py migrate to apply those changes to the database.


# How to access django server on local network 
https://stackoverflow.com/questions/15471173/accessing-django-project-in-lan-systems

################################################################################
# git useful commands
# git status
# git status shows you what files have had changes made to them

# git commit -a -m "insert comment"
# stages commit to become pushed
# need to run git push after commit to make changes to the repository

# git push
# pushes changed files to repository



Currently following youtube django tutorial
https://www.youtube.com/watch?v=WX60HRkfasI
https://www.youtube.com/watch?v=s-ILcyrCzPQ # part 7 on adding delete button
https://www.youtube.com/watch?v=x272Sy9TZ4I # importing excel sheets into ims
