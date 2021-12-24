from django.contrib import admin

# Register your models here.
from .models import Department, Course, Room, OfferedCourses, Semester


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['department_id', 'school_id']


class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_id', 'course_credit', 'course_name', 'department']


class RoomAdmin(admin.ModelAdmin):
    list_display = ['room_id', 'room_capacity']


class OfferedCoursesAdmin(admin.ModelAdmin):
    list_display = ['course', 'course_section', 'course_capacity', 'course_enrolled', 'room_id', 'semester']


class SemesterAdmin(admin.ModelAdmin):
    list_display = ['semester_id', 'semester_name', 'year']


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Semester, SemesterAdmin)
admin.site.register(OfferedCourses, OfferedCoursesAdmin)
