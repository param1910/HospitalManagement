from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect

from .models import users
from  .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.db.models import Q

# Create your views here.


def homepage(request):
  doctors = Doctors.objects.all()
  return render(request,'index.html',{"doctors":doctors})

def dashboard(request):
 return render(request, "patients/dashboard.html")

def book_appointment(request):
  if not(request.user.is_authenticated):
    return redirect("/login")
  if request.method == "POST":
    try:
      appointment = Book_Appointment.objects.create(
        name = request.POST['name'],
        email = request.POST['email'] if request.POST['email'] else "null", 
        age = request.POST['age'], 
        phone_number = request.POST['phone_number'], 
        date = request.POST['date'], 
        doctor_id = request.POST['doctor'], 
        treatment_for = request.POST['treatment_for'], 
      )
      return render(request,"thankyou.html")
    except Exception as e:
      print(e)
      return redirect('/')
    return redirect('/')

def about_us(request):
  return render(request,"about.html")

def get_appointments(request):
  if request.user.is_superuser:
    appointments = Book_Appointment.objects.all()
    query = None
    if request.GET.get('query'):
      query = request.GET.get('query')
      appointments = Book_Appointment.objects.filter(Q(name__icontains = query) | Q(email__icontains = query))
    return render(request,"show_appointments.html",{"appointments":appointments,"query":query})
  return redirect("/")


def delete_appointment(request,appointment_id):
  if request.method == "POST":
    appointment = Book_Appointment.objects.filter(id = appointment_id).delete()
    return redirect("/show-appointments")
  

def edit_appointment(request,appointment_id):
  appointment =Book_Appointment.objects.filter(id = appointment_id)
  if request.method == "POST":
    appointment.update(
      name = request.POST['name'] if request.POST['name'] else appointment.first().name,
      email = request.POST['email'] if request.POST['email'] else appointment.first().email,
      age  = request.POST['age'] if request.POST['age'] else appointment.first().age,
      phone_number = request.POST['phone_number'] if request.POST['phone_number'] else appointment.first().phone_number,
      date = request.POST['date'] if request.POST['date'] else appointment.first().date,
    )
    return redirect("/")
  return render(request,"edit_appointment.html",{"appointment":appointment.first()})



def sample(request):
  return render(request,"sample.html")


# def Login(request):
#   return render(request,"login.html")


def loginHandler(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username,password=password)
    print(user)
    if user is not None:
      login(request,user)
      # login()
      return redirect("/")
    
    return render(request,"login.html")
  return render(request,"login.html")


def signup(request):
      if request.method == "POST":
        first_name=  request.POST['first_name']
        last_name=  request.POST['last_name']
        email = request.POST['email'] 
        username = request.POST['username'] 
        password = request.POST['password']

        user = User.objects.create_user(
          first_name = first_name,
          last_name = last_name,
          email = email,
          username = username,
        )
        user.set_password(password)
        user.save()
        return redirect("/")
      return render(request,"signup.html")  


def edit_user(request):
      if request.method == "POST":
        first_name=  request.POST['first_name']
        last_name=  request.POST['last_name']
        email = request.POST['email'] 
        username = request.POST['username'] 
        password = request.POST['password']
        user = User.objects.filter(username = username)
        user.update(
          first_name = first_name if first_name else user.first().first_name,
          last_name = last_name if last_name else user.first().last_name,
          email = email if email else user.first().email,
          username = username if username else user.first().username,
        )
        return redirect("/")
      return render(request,"signup.html")  

def delete_user(request,user_id):
  if request.method == "POST":
    user = User.objects.filter(id = user_id).delete()
    return redirect("/")
  return redirect("/")


def logoutHandler(request):
  if request.user.is_authenticated:
    logout(request)
    return redirect("/")
  return redirect("/")



def user_appointments(request):
  if request.user.is_authenticated:
    appointment = Book_Appointment.objects.filter(email = request.user.email)
    return render(request,"user_appointmentss.html",{"appointment":appointment.first()})



def booking(request):
  doctors = Doctors.objects.all()
  return render(request,"booking.html",{"doctors":doctors})


def specialities(request):
  return render(request,"specialities.html")

def doctors(request):
  return render(request,"doctorpage.html")


def book_appointment_doc(request):
  if request.method == "POST":
    doctor_name = request.POST['doctor_name']

    


def add_doctor(request):
  if request.method == "POST":
    doctor = Doctors.objects.create(
    name = request.POST['doctor_name'],
    specialization = request.POST['specialization'],
    )    
    return redirect(request.META.get("HTTP_REFERER"))
  
  return render(request,"add_doctor.html")


def get_all_doctors_admin(request):
  if not(request.user.is_superuser):
    return redirect(request.META.get('HTTP_REFERER'))
  doctors = Doctors.objects.all()
  return render(request,"all_doctors.html",{"doctors":doctors})


def delete_doctor(request,doctor_id):
  if request.method == "POST":
    doctor = Doctors.objects.filter(id = doctor_id).delete()
    return redirect(request.META.get('HTTP_REFERER'))


def cancer_care(request):
  return render(request,"cancercare.html")

def HeartVascular(request):
  return render(request,"HeartVascular.html")

def eyecare(request):
  return render(request,"eyecare.html")

def livertrans(request):
  return render(request,"livertrans.html")

def ortho(request):
  return render(request,"ortho.html")

def neuroscience(request):
  return render(request,"neuroscience.html")
def gastro(request):
  return render(request,"gastro.html")





