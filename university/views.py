from django.db import connection
from django.shortcuts import render


# Create your views here.


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def enrollment_view(request):
    semester = connection.cursor()
    semester.execute("SELECT semester_name, year FROM semester")
    semester_query = dictfetchall(semester)

    sets = connection.cursor()
    sets.execute(
        "SELECT DISTINCT offered_courses.semester_id, school_id, SUM(course_enrolled*course.course_credit) AS enrolled "
        "FROM offered_courses "
        "NATURAL JOIN course "
        "NATURAL JOIN department "
        "WHERE school_id ='SETS' "
        "GROUP BY offered_courses.semester_id, school_id")
    sets_query = dictfetchall(sets)

    slass = connection.cursor()
    slass.execute(
        "SELECT DISTINCT offered_courses.semester_id, school_id, SUM(course_enrolled*course.course_credit) AS enrolled "
        "FROM offered_courses "
        "NATURAL JOIN course "
        "NATURAL JOIN department "
        "WHERE school_id ='SLASS' "
        "GROUP BY offered_courses.semester_id, school_id")
    slass_query = dictfetchall(slass)

    sbe = connection.cursor()
    sbe.execute(
        "SELECT DISTINCT offered_courses.semester_id, school_id, SUM(course_enrolled*course.course_credit) AS enrolled "
        "FROM offered_courses "
        "NATURAL JOIN course "
        "NATURAL JOIN department "
        "WHERE school_id ='SBE' "
        "GROUP BY offered_courses.semester_id, school_id")
    sbe_query = dictfetchall(sbe)

    sels = connection.cursor()
    sels.execute(
        "SELECT DISTINCT offered_courses.semester_id, school_id, SUM(course_enrolled*course.course_credit) AS enrolled "
        "FROM offered_courses "
        "NATURAL JOIN course "
        "NATURAL JOIN department "
        "WHERE school_id ='SELS' "
        "GROUP BY offered_courses.semester_id, school_id")
    sels_query = dictfetchall(sels)

    spph = connection.cursor()
    spph.execute(
        "SELECT DISTINCT offered_courses.semester_id, school_id, SUM(course_enrolled*course.course_credit) AS enrolled "
        "FROM offered_courses "
        "NATURAL JOIN course "
        "NATURAL JOIN department "
        "WHERE school_id ='SPPH' "
        "GROUP BY offered_courses.semester_id, school_id")
    spph_query = dictfetchall(spph)

    cse = connection.cursor()
    cse.execute(
        "SELECT DISTINCT offered_courses.semester_id, department.department_id, SUM(course_enrolled*course.course_credit) AS enrolled "
        "FROM offered_courses "
        "NATURAL JOIN course "
        "NATURAL JOIN department "
        "WHERE department.department_id = 'CSE' "
        "GROUP BY offered_courses.semester_id, department.department_id")
    cse_query = dictfetchall(cse)

    eee = connection.cursor()
    eee.execute(
        "SELECT DISTINCT offered_courses.semester_id, department.department_id, SUM(course_enrolled*course.course_credit) AS enrolled "
        "FROM offered_courses "
        "NATURAL JOIN course "
        "NATURAL JOIN department "
        "WHERE department.department_id = 'EEE' "
        "GROUP BY offered_courses.semester_id, department.department_id")
    eee_query = dictfetchall(eee)

    ps = connection.cursor()
    ps.execute(
        "SELECT DISTINCT offered_courses.semester_id, department.department_id, SUM(course_enrolled*course.course_credit) AS enrolled "
        "FROM offered_courses "
        "NATURAL JOIN course "
        "NATURAL JOIN department "
        "WHERE department.department_id = 'PhySci' "
        "GROUP BY offered_courses.semester_id, department.department_id")
    ps_query = dictfetchall(ps)

    school = connection.cursor()
    school.execute(
        "SELECT DISTINCT school_id "
        "FROM offered_courses "
        "NATURAL JOIN course "
        "NATURAL JOIN department "
        "ORDER BY school_id")
    school_query = dictfetchall(school)

    sp2020 = connection.cursor()
    sp2020.execute(
        "SELECT school_id, SUM(course_enrolled*course.course_credit) AS enrolled "
        "FROM offered_courses "
        "NATURAL JOIN course "
        "NATURAL JOIN department "
        "NATURAL JOIN semester "
        "WHERE semester.semester_id=1 "
        "GROUP BY  school_id")
    sp2020_query = dictfetchall(sp2020)

    au2020 = connection.cursor()
    au2020.execute(
        "SELECT school_id, SUM(course_enrolled*course.course_credit) AS enrolled "
        "FROM offered_courses "
        "NATURAL JOIN course "
        "NATURAL JOIN department "
        "NATURAL JOIN semester "
        "WHERE semester.semester_id=2 "
        "GROUP BY  school_id")
    au2020_query = dictfetchall(au2020)

    sp2021 = connection.cursor()
    sp2021.execute(
        "SELECT school_id, SUM(course_enrolled*course.course_credit) AS enrolled "
        "FROM offered_courses "
        "NATURAL JOIN course "
        "NATURAL JOIN department "
        "NATURAL JOIN semester "
        "WHERE semester.semester_id=3 "
        "GROUP BY  school_id")
    sp2021_query = dictfetchall(sp2021)

    su2021 = connection.cursor()
    su2021.execute(
        "SELECT school_id, SUM(course_enrolled*course.course_credit) AS enrolled "
        "FROM offered_courses "
        "NATURAL JOIN course "
        "NATURAL JOIN department "
        "NATURAL JOIN semester "
        "WHERE semester.semester_id=4 "
        "GROUP BY  school_id")
    su2021_query = dictfetchall(su2021)

    au2021 = connection.cursor()
    au2021.execute(
        "SELECT school_id, SUM(course_enrolled*course.course_credit) AS enrolled "
        "FROM offered_courses "
        "NATURAL JOIN course "
        "NATURAL JOIN department "
        "NATURAL JOIN semester "
        "WHERE semester.semester_id=5 "
        "GROUP BY  school_id")
    au2021_query = dictfetchall(au2021)

    sp2020total = connection.cursor()
    sp2020total.execute(
        "SELECT semester_name,year, SUM(course_enrolled*course.course_credit) AS Total "
        "FROM offered_courses "
        "NATURAL JOIN course "
        "NATURAL JOIN department "
        "NATURAL JOIN semester "
        "WHERE semester.semester_id=1 ")
    sp2020total_query = dictfetchall(sp2020total)

    au2020total = connection.cursor()
    au2020total.execute(
        "SELECT semester_name,year, SUM(course_enrolled*course.course_credit) AS Total "
        "FROM offered_courses "
        "NATURAL JOIN course "
        "NATURAL JOIN department "
        "NATURAL JOIN semester "
        "WHERE semester.semester_id=2 ")
    au2020total_query = dictfetchall(au2020total)

    sp2021total = connection.cursor()
    sp2021total.execute(
        "SELECT semester_name,year, SUM(course_enrolled*course.course_credit) AS Total "
        "FROM offered_courses "
        "NATURAL JOIN course "
        "NATURAL JOIN department "
        "NATURAL JOIN semester "
        "WHERE semester.semester_id=3 ")
    sp2021total_query = dictfetchall(sp2021total)

    su2021total = connection.cursor()
    su2021total.execute(
        "SELECT semester_name,year, SUM(course_enrolled*course.course_credit) AS Total "
        "FROM offered_courses "
        "NATURAL JOIN course "
        "NATURAL JOIN department "
        "NATURAL JOIN semester "
        "WHERE semester.semester_id=4 ")
    su2021total_query = dictfetchall(su2021total)

    au2021total = connection.cursor()
    au2021total.execute(
        "SELECT semester_name,year, SUM(course_enrolled*course.course_credit) AS Total "
        "FROM offered_courses "
        "NATURAL JOIN course "
        "NATURAL JOIN department "
        "NATURAL JOIN semester "
        "WHERE semester.semester_id=5 ")
    au2021total_query = dictfetchall(au2021total)

    sp2021change = connection.cursor()
    sp2021change.execute(
        "SELECT semester_name, year, 100* totalChange/SUM(course_enrolled*course.course_credit) AS change "
        "FROM offered_courses, "
        "(SELECT newTotal- SUM(course_enrolled*course.course_credit) as totalChange "
        "FROM offered_courses, "
        "( SELECT SUM(course_enrolled * course.course_credit) as newTotal "
        "FROM offered_courses "
        "NATURAL JOIN course "
        "NATURAL JOIN semester "
        "WHERE semester_id =3  ) AS DevTable2 "
        "NATURAL JOIN course "
        "NATURAL JOIN semester "
        "WHERE semester_id = 1) AS DerivedTable "
        "NATURAL JOIN course "
        "NATURAL JOIN semester "
        "WHERE semester_id = 3"
    )
    sp2021change_query = dictfetchall(sp2021change)

    au2021change = connection.cursor()
    au2021change.execute(
        "SELECT semester_name, year, 100* totalChange/SUM(course_enrolled*course.course_credit) AS change "
        "FROM offered_courses, "
        "(SELECT newTotal- SUM(course_enrolled*course.course_credit) as totalChange "
        "FROM offered_courses, "
        "( SELECT SUM(course_enrolled * course.course_credit) as newTotal "
        "FROM offered_courses "
        "NATURAL JOIN course "
        "NATURAL JOIN semester "
        "WHERE semester_id = 5 ) AS DevTable2 "
        "NATURAL JOIN course "
        "NATURAL JOIN semester "
        "WHERE semester_id = 2) AS DerivedTable "
        "NATURAL JOIN course "
        "NATURAL JOIN semester "
        "WHERE semester_id = 5"
    )
