from django import forms
from .models import departments,room_services, doctors, patients, registration, users

class departmentForm(forms.ModelForm):
    class Meta:
        model=departments
        fields=["department_name"]


class room_servicesForm(forms.ModelForm):
    class Meta:
        model=room_services
        fields=["room_no","ac","tv","sharing"]
        

class doctorsForm(forms.ModelForm):
    class Meta:
        model=doctors
        fields=["doctor_name","department_id"]
        

class patientsForm(forms.ModelForm):
    class Meta:
        model=patients
        fields=["name","fathername","phoneno","emailid","address","gender","age","familymember","relation","dob"]
        

class registrationForm(forms.ModelForm):
    class Meta:
        model=registration
        fields=["date","amount","checkout","history","patient","doctor","roomservices_id"]


class userForm(forms.ModelForm):
    class Meta:
        model=users
        fields=["username", "password"]



        