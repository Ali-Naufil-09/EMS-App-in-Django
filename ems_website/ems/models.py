from django.db import models


#modals are tables and fields are columns

# Create your models here.

class Employee(models.Model):
    GENDER_CHOICES=[('M','Male'),('F','Female'),('O','Others')]
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email_id=models.EmailField(max_length=250)
    phone_number=models.CharField(max_length=200, blank=True) #Blank will appear if anyone does not want to share their number
    address=models.TextField()   #use textfield for unlimited characters
    dob=models.DateField()
    joinning_date=models.DateField()
    gender=models.CharField(max_length=1 , choices=GENDER_CHOICES)
    #defining the relationship b/w both tables
    jobs=models.ManyToManyField('Job', blank=True)
    
    
class Job(models.Model):
    name=models.CharField(max_length=250)
    #to resolve the issue of getting object1 ,object2 instead of jobs on admin server
    def __str__(self):
       return self.name
    
    
#After creating all models(tables), we have to create relationship between tables
#employess------jobs
#1 employee can have more than 1 job. so 1-M  for example an employee can be data analyst and professor and same time 
#jobs----------employees
#1 job can be given to more than 1 employees so it is 1-M   for example there can be 4 web developers in a company      
#hence our relationship is M-M


#after making models we can migrate it
#migrations allow to add,delete,insert data and add,delete,insert (models)tables,columns

#to resolve the issue of getting object1 ,object2 instead of jobs
    def __str__(self):
       return self.name
   
   

