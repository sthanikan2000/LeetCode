# Write your MySQL query statement below
-- select * from (
--     students left join (
--         select student_id,subject_name,count(subject_name) as attended_exams 
--         from examinations group by student_id,subject_name
--     ) Exam_Count using(student_id) 
-- ) as X left join subjects using (subject_name);

-- (select * from students,subjects) 

-- select students.student_id,students.student_name,subjects.subject_name, count(examinations.student_id) 
-- from students,subjects,examinations 
-- where examinations.student_id = students.id and examinations.subject_name = 

select SS.*,IF(ExamCount.attended_exams is null, 0, ExamCount.attended_exams) attended_exams
    from (select * from students,subjects) SS left join 
            (select student_id, subject_name ,count(subject_name) as attended_exams from examinations group by student_id,subject_name) ExamCount
                on SS.student_id=ExamCount.student_id and SS.subject_name=ExamCount.subject_name
                order by SS.student_id,SS.subject_name;