from django.contrib import admin

# Register your models here.

#admin can perform admin operations for example create,update,delete operations
#admin has all previlages
#in order to import modals(tables) in admin.py we can use--
from .models import Employee      #.modals means models.py file
from .models import Job

@admin.register(Employee)     #to register the employee
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','gender','email_id']                                
    
    
#now lets add jobs moddel

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display=['name']  #it displays the name of job rather than object1 , object2, etc