from django.contrib import admin
from django.urls import path
from home import views

app_name = "home"
urlpatterns = [
    path('', views.index, name="home"),
    path('index',views.index_2,name="index"),
    path('login',views.sign_in,name="login"),
    path('instructor_dashboard',views.instructor_dashboard,name="instructor_dashboard"),
    path('instructor_profile_view',views.instructor_profile_view,name="instructor_profile_view"),
    path('my_instructor_profile_view',views.my_instructor_profile_view,name="my_instructor_profile_view"),
    path('all_instructor',views.all_instructor,name="all_instructor"),
    path('student_dashboard',views.student_dashboard,name="student_dashboard"),
    path('about_us',views.about_us,name="about_us"),
    path('contact_us',views.contact_us,name="contact_us"),
    path('sign_up',views.sign_up,name="sign_up"),
    path('sign_in',views.sign_in,name="sign_in"),
    path('my_student_profile_view',views.my_student_profile_view,name="my_student_profile_view"),
    path('courses/<int:course_id>/',views.details,name="details"),
    path('instructor/<int:instructor_id>/',views.instructor_details,name="instructor_details")
]
