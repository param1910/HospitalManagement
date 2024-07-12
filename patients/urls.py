from django.urls import path


from .import views 

urlpatterns=[



path('',views.homepage, name='homepage'),
path('sample',views.sample),
path('logout',views.logoutHandler),
path('login/',views.loginHandler),
path('signup',views.signup),
path('about-us',views.about_us),
path('book-appointment',views.book_appointment),
path('show-appointments',views.get_appointments),
path('appointment/<int:appointment_id>/delete',views.delete_appointment),
path('appointment/<int:appointment_id>/edit',views.edit_appointment),
path('booking',views.booking),
path('specialities',views.specialities),
path('doctors',views.doctors),
path('doctors/all',views.get_all_doctors_admin),
path('doctors/<int:doctor_id>/delete',views.delete_doctor),
path('doctors/add',views.add_doctor),
path("gastro",views.gastro),
path("neuroscience",views.neuroscience),
path("ortho",views.ortho),
path("livertrans",views.livertrans),
path("cancer_care",views.cancer_care),
path("eyecare",views.eyecare),
path("HeartVascular",views.HeartVascular),
# path('doctors/book-appointment',views.),
]