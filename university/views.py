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
au2021change_query = dictfetchall(au2021change)

    context = {'semester_query': semester_query, 'sets': sets_query, 'slass': slass_query, 'sbe': sbe_query,
               'sels': sels_query, 'spph': spph_query, 'cse': cse_query, 'eee': eee_query, 'ps': ps_query,
               'school': school_query, 'sp2020': sp2020_query, 'au2020': au2020_query, 'sp2021': sp2021_query,
               'su2021': su2021_query, 'au2021': au2021_query, 'sp2020total': sp2020total_query,
               'au2020total': au2020total_query,
               'sp2021total': sp2021total_query, 'su2021total': su2021total_query, 'au2021total': au2021total_query,
               'sp2021change': sp2021change_query, 'au2021change': au2021change_query}
    return render(request, 'enrollment.html', context)


def class_size_view(request):
    sp2021class = connection.cursor()
    sp2021class.execute(
        """ 
        SELECT "1-10" AS classzie, COUNT(course_section) AS section, COUNT(course_section)/12 AS class6, COUNT(course_section)/14 AS class7
        FROM offered_courses
        WHERE course_enrolled > 0 AND course_enrolled <= 10 AND semester_id=3
        UNION
        SELECT "11-20" AS classzie, COUNT(course_section) AS section, COUNT(course_section)/12 AS class6, COUNT(course_section)/14 AS class7
        FROM offered_courses
        WHERE course_enrolled > 10 AND course_enrolled <= 20 AND semester_id=3
        UNION
        SELECT "21-30" AS classzie,COUNT(course_section) AS section, COUNT(course_section)/12 AS class6, COUNT(course_section)/14 AS class7
        FROM offered_courses
        WHERE course_enrolled > 20 AND course_enrolled <= 30 AND semester_id=3
        UNION
        SELECT "31-35" AS classzie,COUNT(course_section) AS section, COUNT(course_section)/12 AS class6, COUNT(course_section)/14 AS class7
        FROM offered_courses
        WHERE course_enrolled > 30 AND course_enrolled <= 35 AND semester_id=3
        UNION
        SELECT "36-40" AS classzie,COUNT(course_section) AS section, COUNT(course_section)/12 AS class6, COUNT(course_section)/14 AS class7
        FROM offered_courses
        WHERE course_enrolled > 35 AND course_enrolled <=40 AND semester_id=3
        UNION
        SELECT "41-50" AS classzie,COUNT(course_section) AS section, COUNT(course_section)/12 AS class6, COUNT(course_section)/14 AS class7
        FROM offered_courses
        WHERE course_enrolled > 40 AND course_enrolled <= 50 AND semester_id=3
        UNION
        SELECT "51-55" AS classzie,COUNT(course_section) AS section, COUNT(course_section)/12 AS class6, COUNT(course_section)/14 AS class7
        FROM offered_courses
        WHERE course_enrolled > 50 AND course_enrolled <= 55 AND semester_id=3
        UNION
        SELECT "56-65" AS classzie,COUNT(course_section) AS section, COUNT(course_section)/12 AS class6, COUNT(course_section)/14 AS class7
        FROM offered_courses
        WHERE course_enrolled > 55 AND course_enrolled <= 65 AND semester_id=3 
        UNION
        SELECT "TOTAL" AS classzie, SUM(section) AS section, SUM(class6) AS class6, SUM(class7) AS class7
        FROM sp2021class
 """
    )

    sp2021class_query = dictfetchall(sp2021class)

    su2021class = connection.cursor()
    su2021class.execute(
        """
        SELECT "1-10" AS classzie, COUNT(course_section) AS section, COUNT(course_section)/12 AS class6, COUNT(course_section)/14 AS class7
        FROM offered_courses
        WHERE course_enrolled > 0 AND course_enrolled <= 10 AND semester_id=4
        UNION
        SELECT "11-20" AS classzie, COUNT(course_section) AS section, COUNT(course_section)/12 AS class6, COUNT(course_section)/14 AS class7
        FROM offered_courses
        WHERE course_enrolled > 10 AND course_enrolled <= 20 AND semester_id=4
        UNION
        SELECT "21-30" AS classzie,COUNT(course_section) AS section, COUNT(course_section)/12 AS class6, COUNT(course_section)/14 AS class7
        FROM offered_courses
        WHERE course_enrolled > 20 AND course_enrolled <= 30 AND semester_id=4
        UNION
        SELECT "31-35" AS classzie,COUNT(course_section) AS section, COUNT(course_section)/12 AS class6, COUNT(course_section)/14 AS class7
        FROM offered_courses
        WHERE course_enrolled > 30 AND course_enrolled <= 35 AND semester_id=4
        UNION
        SELECT "36-40" AS classzie,COUNT(course_section) AS section, COUNT(course_section)/12 AS class6, COUNT(course_section)/14 AS class7
        FROM offered_courses
        WHERE course_enrolled > 35 AND course_enrolled <=40 AND semester_id=4
        UNION
        SELECT "41-50" AS classzie,COUNT(course_section) AS section, COUNT(course_section)/12 AS class6, COUNT(course_section)/14 AS class7
        FROM offered_courses
        WHERE course_enrolled > 40 AND course_enrolled <= 50 AND semester_id=4
        UNION
        SELECT "51-55" AS classzie,COUNT(course_section) AS section, COUNT(course_section)/12 AS class6, COUNT(course_section)/14 AS class7
        FROM offered_courses
        WHERE course_enrolled > 50 AND course_enrolled <= 55 AND semester_id=4
        UNION
        SELECT "56-55" AS classzie,COUNT(course_section) AS section, COUNT(course_section)/12 AS class6, COUNT(course_section)/14 AS class7
        FROM offered_courses
        WHERE course_enrolled > 55 AND course_enrolled <= 65 AND semester_id=4
        UNION
        SELECT "TOTAL" AS classzie, SUM(section) AS section, SUM(class6) AS class6, SUM(class7) AS class7
        FROM su2021class
        """
    )

    su2021class_query = dictfetchall(su2021class)

    sp2021piechart = connection.cursor()
    sp2021piechart.execute(
        """SELECT * FROM sp2021class"""
    )
    sp2021piechart_query = dictfetchall(sp2021piechart)

    su2021piechart = connection.cursor()
    su2021piechart.execute(
        """SELECT * FROM su2021class"""
    )
    su2021piechart_query = dictfetchall(su2021piechart)

    sp2021en1 = connection.cursor()
    sp2021en1.execute(
        """
        SELECT department.school_id, section
FROM department
LEFT JOIN sp2021en1 s on department.school_id = s.school_id
GROUP BY department.school_id
UNION
SELECT  "total" as school_id, SUM(section)
FROM sp2021en1
        """
    )
    sp2021en1_query = dictfetchall(sp2021en1)

    sp2021en2 = connection.cursor()
    sp2021en2.execute(
        """
        SELECT department.school_id, section
FROM department
LEFT JOIN sp2021en2 s on department.school_id = s.school_id
GROUP BY department.school_id
UNION
SELECT  "total" as school_id, SUM(section)
FROM sp2021en2
        """
    )
    sp2021en2_query = dictfetchall(sp2021en2)

    sp2021en3 = connection.cursor()
    sp2021en3.execute(
        """
        SELECT department.school_id, section
FROM department
LEFT JOIN sp2021en3 s on department.school_id = s.school_id
GROUP BY department.school_id
UNION
SELECT  "total" as school_id, SUM(section)
FROM sp2021en3
        """
    )
    sp2021en3_query = dictfetchall(sp2021en3)

    sp2021en4 = connection.cursor()
    sp2021en4.execute(
        """
        SELECT department.school_id, section
FROM department
LEFT JOIN sp2021en4 s on department.school_id = s.school_id
GROUP BY department.school_id
UNION
SELECT  "total" as school_id, SUM(section)
FROM sp2021en4
        """
    )
    sp2021en4_query = dictfetchall(sp2021en4)

    sp2021en5 = connection.cursor()
    sp2021en5.execute(
        """
        SELECT department.school_id, section
FROM department
LEFT JOIN sp2021en5 s on department.school_id = s.school_id
GROUP BY department.school_id
UNION
SELECT  "total" as school_id, SUM(section)
FROM sp2021en5
        """
    )
    sp2021en5_query = dictfetchall(sp2021en5)

    sp2021en6 = connection.cursor()
    sp2021en6.execute(
        """
       SELECT department.school_id, section
FROM department
LEFT JOIN sp2021en6 s on department.school_id = s.school_id
GROUP BY department.school_id
UNION
SELECT  "total" as school_id, SUM(section)
FROM sp2021en6
        """
    )
    sp2021en6_query = dictfetchall(sp2021en6)

    sp2021en7 = connection.cursor()
    sp2021en7.execute(
        """
       SELECT department.school_id, section
FROM department
LEFT JOIN sp2021en7 s on department.school_id = s.school_id
GROUP BY department.school_id
UNION
SELECT  "total" as school_id, SUM(section)
FROM sp2021en7
        """
    )
    sp2021en7_query = dictfetchall(sp2021en7)

    sp2021en8 = connection.cursor()
    sp2021en8.execute(
        """
       SELECT department.school_id, section
FROM department
LEFT JOIN sp2021en8 s on department.school_id = s.school_id
GROUP BY department.school_id
UNION
SELECT  "total" as school_id, SUM(section)
FROM sp2021en8
        """
    )
    sp2021en8_query = dictfetchall(sp2021en8)

    sp2021en9 = connection.cursor()
    sp2021en9.execute(
        """
       SELECT department.school_id, section
FROM department
LEFT JOIN sp2021en9 s on department.school_id = s.school_id
GROUP BY department.school_id
UNION
SELECT  "total" as school_id, SUM(section)
FROM sp2021en9
        """
    )
    sp2021en9_query = dictfetchall(sp2021en9)

    su2021en1 = connection.cursor()
    su2021en1.execute(
        """
        SELECT department.school_id, section
FROM department
LEFT JOIN su2021en1 s on department.school_id = s.school_id
GROUP BY department.school_id
UNION
SELECT  "total" as school_id, SUM(section)
FROM su2021en1
        """
    )
su2021en1_query = dictfetchall(su2021en1)

    su2021en2 = connection.cursor()
    su2021en2.execute(
        """
        SELECT department.school_id, section
FROM department
LEFT JOIN su2021en2 s on department.school_id = s.school_id
GROUP BY department.school_id
UNION
SELECT  "total" as school_id, SUM(section)
FROM su2021en2
        """
    )
    su2021en2_query = dictfetchall(su2021en2)

    su2021en3 = connection.cursor()
    su2021en3.execute(
        """
        SELECT department.school_id, section
FROM department
LEFT JOIN su2021en3 s on department.school_id = s.school_id
GROUP BY department.school_id
UNION
SELECT  "total" as school_id, SUM(section)
FROM su2021en3
        """
    )
    su2021en3_query = dictfetchall(su2021en3)

    su2021en4 = connection.cursor()
    su2021en4.execute(
        """
        SELECT department.school_id, section
FROM department
LEFT JOIN su2021en4 s on department.school_id = s.school_id
GROUP BY department.school_id
UNION
SELECT  "total" as school_id, SUM(section)
FROM su2021en4
        """
    )
    su2021en4_query = dictfetchall(su2021en4)

    su2021en5 = connection.cursor()
    su2021en5.execute(
        """
        SELECT department.school_id, section
FROM department
LEFT JOIN su2021en5 s on department.school_id = s.school_id
GROUP BY department.school_id
UNION
SELECT  "total" as school_id, SUM(section)
FROM su2021en5
        """
    )
    su2021en5_query = dictfetchall(su2021en5)

    su2021en6 = connection.cursor()
    su2021en6.execute(
        """
        SELECT department.school_id, section
FROM department
LEFT JOIN su2021en6 s on department.school_id = s.school_id
GROUP BY department.school_id
UNION
SELECT  "total" as school_id, SUM(section)
FROM su2021en6
        """
    )
    su2021en6_query = dictfetchall(su2021en6)

    su2021en7 = connection.cursor()
    su2021en7.execute(
        """
       SELECT department.school_id, section
FROM department
LEFT JOIN su2021en7 s on department.school_id = s.school_id
GROUP BY department.school_id
UNION
SELECT  "total" as school_id, SUM(section)
FROM su2021en7
        """
    )
    su2021en7_query = dictfetchall(su2021en7)

    su2021en8 = connection.cursor()
    su2021en8.execute(
        """
       select department.school_id, no_of_sec as section
from department
left join su2021en8 s on department.school_id = s.school_id
group by department.school_id
UNION
SELECT  "total" as school_id, sum(no_of_sec) as section
from su2021en8
        """
    )
    su2021en8_query = dictfetchall(su2021en8)

    su2021en9 = connection.cursor()
    su2021en9.execute(
        """
       select department.school_id, section
from department
left join su2021en9 s on department.school_id = s.school_id
group by department.school_id
UNION
SELECT  "total" as school_id, count(section)
from su2021en9
        """
    )
    su2021en9_query = dictfetchall(su2021en9)

    sp2021bar1 = connection.cursor()
    sp2021bar1.execute(
        """
        SELECT school_id, COUNT(course_section) AS section, "1-10" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 0 AND course_enrolled <= 10  AND semester_id = 3 AND school_id="SBE"
UNION
SELECT school_id, COUNT(course_section) AS section, "11-20" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 10 AND course_enrolled <= 20  AND semester_id = 3 AND school_id="SBE"
UNION
SELECT school_id, COUNT(course_section) AS section, "21-30" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 20 AND course_enrolled <= 30  AND semester_id = 3 AND school_id="SBE"
UNION
SELECT school_id, COUNT(course_section) AS section, "31-35" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 30 AND course_enrolled <= 35  AND semester_id = 3 AND school_id="SBE"
UNION
SELECT school_id, COUNT(course_section) AS section, "36-40" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 35 AND course_enrolled <= 40  AND semester_id = 3 AND school_id="SBE"
UNION
SELECT school_id, COUNT(course_section) AS section, "41-50" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 40 AND course_enrolled <= 50  AND semester_id = 3 AND school_id="SBE"
UNION
SELECT school_id, COUNT(course_section) AS section, "51-55" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 50 AND course_enrolled <= 55  AND semester_id = 3 AND school_id="SBE"
UNION
SELECT school_id, COUNT(course_section) AS section, "56-60" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 55 AND course_enrolled <= 60  AND semester_id = 3 AND school_id="SBE"
UNION
SELECT school_id, COUNT(course_section) AS section, "60+" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 60 AND semester_id = 3 AND school_id="SBE"
ORDER BY classize
        """
    )
    sp2021bar1_query = dictfetchall(sp2021bar1)

    sp2021bar2 = connection.cursor()
    sp2021bar2.execute(
        """
        SELECT school_id, COUNT(course_section) AS section, "1-10" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 0 AND course_enrolled <= 10  AND semester_id = 3 AND school_id="SELS"
UNION
SELECT school_id, COUNT(course_section) AS section, "11-20" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 10 AND course_enrolled <= 20  AND semester_id = 3 AND school_id="SELS"
UNION
SELECT school_id, COUNT(course_section) AS section, "21-30" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 20 AND course_enrolled <= 30  AND semester_id = 3 AND school_id="SELS"
UNION
SELECT school_id, COUNT(course_section) AS section, "31-35" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 30 AND course_enrolled <= 35  AND semester_id = 3 AND school_id="SELS"
UNION
SELECT school_id, COUNT(course_section) AS section, "36-40" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 35 AND course_enrolled <= 40  AND semester_id = 3 AND school_id="SELS"
UNION
SELECT school_id, COUNT(course_section) AS section, "41-50" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 40 AND course_enrolled <= 50  AND semester_id = 3 AND school_id="SELS"
UNION
SELECT school_id, COUNT(course_section) AS section, "51-55" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 50 AND course_enrolled <= 55  AND semester_id = 3 AND school_id="SELS"
UNION
SELECT school_id, COUNT(course_section) AS section, "56-60" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 55 AND course_enrolled <= 60  AND semester_id = 3 AND school_id="SELS"
UNION
SELECT school_id, COUNT(course_section) AS section, "60+" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 60 AND semester_id = 3 AND school_id="SELS"
ORDER BY classize
        """
    )
    sp2021bar2_query = dictfetchall(sp2021bar2)

    sp2021bar3 = connection.cursor()
    sp2021bar3.execute(
        """
        SELECT school_id, COUNT(course_section) AS section, "1-10" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 0 AND course_enrolled <= 10  AND semester_id = 3 AND school_id="SETS"
UNION
SELECT school_id, COUNT(course_section) AS section, "11-20" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 10 AND course_enrolled <= 20  AND semester_id = 3 AND school_id="SETS"
UNION
SELECT school_id, COUNT(course_section) AS section, "21-30" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 20 AND course_enrolled <= 30  AND semester_id = 3 AND school_id="SETS"
UNION
SELECT school_id, COUNT(course_section) AS section, "31-35" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 30 AND course_enrolled <= 35  AND semester_id = 3 AND school_id="SETS"
UNION
SELECT school_id, COUNT(course_section) AS section, "36-40" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 35 AND course_enrolled <= 40  AND semester_id = 3 AND school_id="SETS"
UNION
SELECT school_id, COUNT(course_section) AS section, "41-50" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 40 AND course_enrolled <= 50  AND semester_id = 3 AND school_id="SETS"
UNION
SELECT school_id, COUNT(course_section) AS section, "51-55" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 50 AND course_enrolled <= 55  AND semester_id = 3 AND school_id="SETS"
UNION
SELECT school_id, COUNT(course_section) AS section, "56-60" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 55 AND course_enrolled <= 60  AND semester_id = 3 AND school_id="SETS"
UNION
SELECT school_id, COUNT(course_section) AS section, "60+" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 60 AND semester_id = 3 AND school_id="SETS"
ORDER BY classize
        """
    )
    sp2021bar3_query = dictfetchall(sp2021bar3)

    sp2021bar4 = connection.cursor()
    sp2021bar4.execute(
        """
        SELECT school_id, COUNT(course_section) AS section, "1-10" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 0 AND course_enrolled <= 10  AND semester_id = 3 AND school_id="SLASS"
UNION
SELECT school_id, COUNT(course_section) AS section, "11-20" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 10 AND course_enrolled <= 20  AND semester_id = 3 AND school_id="SLASS"
UNION
SELECT school_id, COUNT(course_section) AS section, "21-30" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 20 AND course_enrolled <= 30  AND semester_id = 3 AND school_id="SLASS"
UNION
SELECT school_id, COUNT(course_section) AS section, "31-35" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 30 AND course_enrolled <= 35  AND semester_id = 3 AND school_id="SLASS"
UNION
SELECT school_id, COUNT(course_section) AS section, "36-40" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 35 AND course_enrolled <= 40  AND semester_id = 3 AND school_id="SLASS"
UNION
SELECT school_id, COUNT(course_section) AS section, "41-50" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 40 AND course_enrolled <= 50  AND semester_id = 3 AND school_id="SLASS"
UNION
SELECT school_id, COUNT(course_section) AS section, "51-55" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 50 AND course_enrolled <= 55  AND semester_id = 3 AND school_id="SLASS"
UNION
SELECT school_id, COUNT(course_section) AS section, "56-60" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 55 AND course_enrolled <= 60  AND semester_id = 3 AND school_id="SLASS"
UNION
SELECT school_id, COUNT(course_section) AS section, "60+" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 60 AND semester_id = 3 AND school_id="SLASS"
ORDER BY classize
        """
    )
    sp2021bar4_query = dictfetchall(sp2021bar4)

    sp2021bar5 = connection.cursor()
    sp2021bar5.execute(
        """
        SELECT school_id, COUNT(course_section) AS section, "1-10" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 0 AND course_enrolled <= 10  AND semester_id = 3 AND school_id="SPPH"
UNION
SELECT school_id, COUNT(course_section) AS section, "11-20" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 10 AND course_enrolled <= 20  AND semester_id = 3 AND school_id="SPPH"
UNION
SELECT school_id, COUNT(course_section) AS section, "21-30" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 20 AND course_enrolled <= 30  AND semester_id = 3 AND school_id="SPPH"
UNION
SELECT school_id, COUNT(course_section) AS section, "31-35" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 30 AND course_enrolled <= 35  AND semester_id = 3 AND school_id="SPPH"
UNION
SELECT school_id, COUNT(course_section) AS section, "36-40" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 35 AND course_enrolled <= 40  AND semester_id = 3 AND school_id="SPPH"
UNION
SELECT school_id, COUNT(course_section) AS section, "41-50" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 40 AND course_enrolled <= 50  AND semester_id = 3 AND school_id="SPPH"
UNION
SELECT school_id, COUNT(course_section) AS section, "51-55" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 50 AND course_enrolled <= 55  AND semester_id = 3 AND school_id="SPPH"
UNION
SELECT school_id, COUNT(course_section) AS section, "56-60" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 55 AND course_enrolled <= 60  AND semester_id = 3 AND school_id="SPPH"
UNION
SELECT school_id, COUNT(course_section) AS section, "60+" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 60 AND semester_id = 3 AND school_id="SPPH"
ORDER BY classize
        """
    )
    sp2021bar5_query = dictfetchall(sp2021bar5)

    su2021bar1 = connection.cursor()
    su2021bar1.execute(
        """
        SELECT school_id, COUNT(course_section) AS section, "1-10" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 0 AND course_enrolled <= 10  AND semester_id = 4 AND school_id="SBE"
UNION
SELECT school_id, COUNT(course_section) AS section, "11-20" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 10 AND course_enrolled <= 20  AND semester_id = 4 AND school_id="SBE"
UNION
SELECT school_id, COUNT(course_section) AS section, "21-30" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 20 AND course_enrolled <= 30  AND semester_id = 4 AND school_id="SBE"
UNION
SELECT school_id, COUNT(course_section) AS section, "31-35" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 30 AND course_enrolled <= 35  AND semester_id = 4 AND school_id="SBE"
UNION
SELECT school_id, COUNT(course_section) AS section, "36-40" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 35 AND course_enrolled <= 40  AND semester_id = 4 AND school_id="SBE"
UNION
SELECT school_id, COUNT(course_section) AS section, "41-50" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 40 AND course_enrolled <= 50  AND semester_id = 4 AND school_id="SBE"
UNION
SELECT school_id, COUNT(course_section) AS section, "51-55" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 50 AND course_enrolled <= 55  AND semester_id = 4 AND school_id="SBE"
UNION
SELECT school_id, COUNT(course_section) AS section, "56-60" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 55 AND course_enrolled <= 60  AND semester_id = 4 AND school_id="SBE"
UNION
SELECT school_id, COUNT(course_section) AS section, "60+" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 60 AND semester_id = 4 AND school_id="SBE"
ORDER BY classize
        """
    )
    su2021bar1_query = dictfetchall(su2021bar1)

    su2021bar2 = connection.cursor()
    su2021bar2.execute(
        """
        SELECT school_id, COUNT(course_section) AS section, "1-10" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 0 AND course_enrolled <= 10  AND semester_id = 4 AND school_id="SELS"
UNION
SELECT school_id, COUNT(course_section) AS section, "11-20" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 10 AND course_enrolled <= 20  AND semester_id = 4 AND school_id="SELS"
UNION
SELECT school_id, COUNT(course_section) AS section, "21-30" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 20 AND course_enrolled <= 30  AND semester_id = 4 AND school_id="SELS"
UNION
SELECT school_id, COUNT(course_section) AS section, "31-35" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 30 AND course_enrolled <= 35  AND semester_id = 4 AND school_id="SELS"
UNION
SELECT school_id, COUNT(course_section) AS section, "36-40" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 35 AND course_enrolled <= 40  AND semester_id = 4 AND school_id="SELS"
UNION
SELECT school_id, COUNT(course_section) AS section, "41-50" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 40 AND course_enrolled <= 50  AND semester_id = 4 AND school_id="SELS"
UNION
SELECT school_id, COUNT(course_section) AS section, "51-55" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 50 AND course_enrolled <= 55  AND semester_id = 4 AND school_id="SELS"
UNION
SELECT school_id, COUNT(course_section) AS section, "56-60" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 55 AND course_enrolled <= 60  AND semester_id = 4 AND school_id="SELS"
UNION
SELECT school_id, COUNT(course_section) AS section, "60+" as classize
FROM offered_courses
NATURAL JOIN course
NATURAL JOIN department
WHERE course_enrolled > 60 AND semester_id = 4 AND school_id="SELS"
ORDER BY classize
        """
    )
