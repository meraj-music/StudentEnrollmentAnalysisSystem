from django.db import models


# Create your models here.

class Department(models.Model):
    department_id = models.CharField(max_length=10, primary_key=True)
    school_id = models.CharField(max_length=10)

    def __str__(self):
        return str(self.department_id)

    class Meta:
        ordering = ['department_id']
        db_table = "department"


class Course(models.Model):
    course_id = models.CharField(max_length=10, primary_key=True)
    course_credit = models.IntegerField()
    course_name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=False)

    def __str__(self):
        return str(self.course_id)

    class Meta:
        ordering = ['course_id']
        db_table = "course"


class Room(models.Model):
    room_id = models.CharField(max_length=20, primary_key=True)
    room_capacity = models.IntegerField()

    def __str__(self):
        return str(self.room_id)

    class Meta:
        ordering = ['room_id']
        db_table = "room"


class Semester(models.Model):
    semester_id = models.IntegerField(primary_key=True)
    semester_name = models.CharField(max_length=10, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.semester_name+str(self.year)

    class Meta:
        ordering = ['semester_id']
        db_table = "semester"


class OfferedCourses(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=False)
    course_section = models.IntegerField()
    course_capacity = models.IntegerField()
    course_enrolled = models.IntegerField()
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True)
    semester = models.ForeignKey(Semester, on_delete=models.SET_NULL, null=True, blank=False)

    def __str__(self):
        return str(self.course)

    class Meta:
        ordering = ['course', 'course_section', 'semester']
        db_table = "offered_courses"
