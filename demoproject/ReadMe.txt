Creating Super User:

python .\manage.py createsuperuser





python .\manage.py makemigrations

python .\manage.py migrate



python .\manage.py sqlmigrate myapp 0001

Url tag- {% %}

python .\manage.py shell
from myapp.models import Student
std = Student.objects.all()
std
Student.objects.get_or_create(name = 'shuvo',email='shuvo@t.com',dob='1992-08-26')

#to exit from shell:
quit()

pip install faker

python .\SeedData.py  