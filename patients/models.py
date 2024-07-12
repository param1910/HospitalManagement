from django.db import models

# Create your models here.


class users(models.Model):
    username=models.CharField(max_length=25,default="")
    password=models.CharField(max_length=25,default="")
    status=models.CharField(max_length=25,default="")


class Doctors(models.Model):
    name = models.CharField(max_length=300)
    specialization = models.CharField(max_length=300)



class Book_Appointment(models.Model):
    class Meta:
        db_table = "Book_Appointment"

    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True,null=True)
    phone_number = models.CharField(max_length=12)
    age = models.CharField(max_length=4)
    date = models.CharField(max_length=16)
    treatment_for = models.TextField()
    doctor =  models.ForeignKey(Doctors,on_delete=models.CASCADE)




   

    
