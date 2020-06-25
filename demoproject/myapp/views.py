from django.shortcuts import render

from myapp.models import Student

def index(request):
    return render(request,'index.html')

def list(request):
    std= Student.objects.all()
    context = {'students':std,'title':'List'}
    return render(request,'list.html',context)


