from django.shortcuts import render, HttpResponse
from .models import allCourses,allInstructors
# Create your views here.
def index(request):
    getCourse = allCourses.objects.all()
    return render(request,"home/explore.html",{'getCourse':getCourse})

def index_2(request):
    return render(request,"home/index-2.html")

def sign_in(request):
    return render(request,"home/sign_in.html")

def instructor_dashboard(request):
    return render(request,"home/instructor_dashboard.html")

def instructor_profile_view(request):
    return render(request,"home/instructor_profile_view.html")

def my_instructor_profile_view(request):
    return render(request,"home/my_instructor_profile_view.html")

def all_instructor(request):
    return render(request,"home/all_instructor.html")

def student_dashboard(request):
    return render(request,"home/student_dashboard.html")

def about_us(request):
    return render(request,"home/about_us.html")

def contact_us(request):
    return render(request,"home/contact_us.html")

def sign_up(request):
    return render(request,"home/sign_up.html")

def sign_in(request):
    return render(request,"home/sign_in.html")

def my_student_profile_view(request):
    return render(request,"home/my_student_profile_view.html")

def details(request,course_id):
    getCourse = allCourses.objects.get(pk=course_id)
    return render(request,'home/coursedetails.html',{'getCourse':getCourse})

def instructor_details(request,instructor_id):
    instructor = allInstructors.objects.get(pk=instructor_id)
    return render(request,'home/instructor_profile_view.html',{'instructor':instructor})