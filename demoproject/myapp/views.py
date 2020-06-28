from django.shortcuts import render

from myapp.models import Student

from django.core.paginator import Paginator

def index(request):
    return render(request,'index.html')

def list(request):
    std= Student.objects.all()
    #paging
    paginator = Paginator(std,5)
    page = request.GET.get('page')
    stdents = paginator.get_page(page)
    context = {'students':stdents,'title':'List'}
    return render(request,'list.html',context)

def create(request):
    return render(request,'create.html')


