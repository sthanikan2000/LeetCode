# Write your MySQL query statement below
SELECT s.student_id, s.student_name, sub.subject_name, COUNT(e.student_id) AS attended_exams
-- select *
FROM Students s 
CROSS JOIN Subjects sub
LEFT JOIN Examinations e ON s.student_id = e.student_id AND sub.subject_name = e.subject_name
GROUP BY s.student_id, sub.subject_name
ORDER BY s.student_id, sub.subject_name;


-- select SS.*,IF(ExamCount.attended_exams is null, 0, ExamCount.attended_exams) attended_exams
--     from (select * from students,subjects) SS left join 
--             (select student_id, subject_name ,count(subject_name) as attended_exams from examinations group by student_id,subject_name) ExamCount
--                 on SS.student_id=ExamCount.student_id and SS.subject_name=ExamCount.subject_name
--                 order by SS.student_id,SS.subject_name;