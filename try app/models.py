from django.db import models

# Create your models here.


class allInstructors(models.Model):
    def __str__(self):
        return self.instructor_name

    instructor_name = models.CharField(max_length=100,default="")
    instructor_email = models.CharField(max_length=100,default="")
    total_courses = models.IntegerField(default=0)
    desc = models.CharField(max_length = 5000,default="")


class allCourses(models.Model):

    def __str__(self):
        return self.course_name
    
    course_name = models.CharField(max_length=100)
    course_subheading = models.CharField(max_length=500,default="")
    course_desc = models.CharField(max_length=5000)
    course_date = models.DateField(auto_now=True)
    course_image = models.CharField(max_length=5000,default="")
    course_rating = models.FloatField(default=0.0)
    course_total_ratings = models.IntegerField(default=0)
    course_enrollment = models.IntegerField(default=0)
    course_instructor = models.ForeignKey(allInstructors,on_delete=models.CASCADE,null=True)
    