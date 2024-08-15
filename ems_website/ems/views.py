from django.shortcuts import render
from django.http import Http404
from .models import Employee

# Create your views here.

#Urls-------Url patterns-------Views------Templates
#Views has linker functions that links to templates

def home(request):
   employees=Employee.objects.all()
   return render(request,'ems/home.html',{'employees':employees})

#render() function passes the data to html templates In my case template is named  home.html in ems folder(front-end)

def employee_detail(request,employee_id):
 try:                                        #try is used because we wnat to show user that employee 6,7,8 not exits
    e=Employee.objects.get(id=employee_id)
 except Employee.DoesNotExist:
    raise Http404('Emploee not found')
 return render(request,'ems/employee_detail.html',{'employee':e})  #we will call objects in html files by employee because we said 'employee'=e
    