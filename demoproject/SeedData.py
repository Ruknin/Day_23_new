import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demoproject.settings')

import django
django.setup()

from myapp.models import Student
from faker import Faker

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

fk = Faker()

def addstudent():
    fname=fk.name()
    femail=fk.email()
    fdob=fk.date()
    Student.objects.get_or_create(name=fname,email=femail,dob=fdob)

def populatedata(n=5):
    for entry in range(n):
        addstudent()



def makesuperuser(un,pw,em,fn,ln):
    User.objects.get_or_create(
        username= un,
        password= make_password(pw),
        email=em,
        first_name=fn,
        last_name= ln,
        is_staff=True,
        is_superuser=True,
        is_active=True
    )

try:
    makesuperuser('admin','1234','admin@gmail.com','Ruknin','Shadid')
    print('Superuser Created Sucessfully ')
    print(50*'#')
except:
    print('Superuser Already exist!!!')

print('Populating Data, Please wait...')
print(50*'#')

populatedata(30)

print('Populating Data Complete')
print(50*'#')