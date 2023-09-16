/*  1   */
select * from ПРЕПОДАВАТЕЛЬ

/*  2   */
select * from СТУДЕНЧЕСКАЯ_ГРУППА
where Специальность = 'ЭВМ'

/*  3   */
select ЛичныйНомер, НомерАудитории 
    from ПРЕПОДАВАТЕЛЬ_ПРЕПОДАЕТ_ПРЕДМЕТЫ_В_ГРУППАХ
where КодовыйНомерПредмета = '18П'

/*  4   */
select distinct sub_t.КодовыйНомерПредмета, sub_t.НазваниеПредмета 
    from ПРЕПОДАВАТЕЛЬ_ПРЕПОДАЕТ_ПРЕДМЕТЫ_В_ГРУППАХ teacher_sub_t
left join ПРЕДМЕТ sub_t 
    on teacher_sub_t.КодовыйНомерПредмета = sub_t.КодовыйНомерПредмета
left join ПРЕПОДАВАТЕЛЬ teacher_t 
    on teacher_sub_t.ЛичныйНомер = teacher_t.ЛичныйНомер
where teacher_t.Фамилия = 'Костин'

/*  5   */
select teacher_sub.КодовыйНомерГруппы 
    from ПРЕПОДАВАТЕЛЬ_ПРЕПОДАЕТ_ПРЕДМЕТЫ_В_ГРУППАХ teacher_sub
left join ПРЕПОДАВАТЕЛЬ teacher
    on teacher_sub.ЛичныйНомер = teacher.ЛичныйНомер
where teacher.Фамилия = 'Фролов'

/*  6   */
select distinct sub.*
	from ПРЕПОДАВАТЕЛЬ_ПРЕПОДАЕТ_ПРЕДМЕТЫ_В_ГРУППАХ teacher_sub
left join ПРЕДМЕТ sub
	on teacher_sub.КодовыйНомерПредмета = sub.КодовыйНомерПредмета
left join СТУДЕНЧЕСКАЯ_ГРУППА gr
	on teacher_sub.КодовыйНомерГруппы = gr.КодовыйНомерГруппы
where gr.Специальность = 'АСОИ'

/*  7   */
select distinct teacher.*
	from ПРЕПОДАВАТЕЛЬ_ПРЕПОДАЕТ_ПРЕДМЕТЫ_В_ГРУППАХ teacher_sub
left join ПРЕПОДАВАТЕЛЬ teacher
	on teacher_sub.ЛичныйНомер = teacher.ЛичныйНомер
left join СТУДЕНЧЕСКАЯ_ГРУППА gr
	on teacher_sub.КодовыйНомерГруппы = gr.КодовыйНомерГруппы
where gr.Специальность = 'АСОИ'

/*  8   */
select distinct teacher.Фамилия
	from ПРЕПОДАВАТЕЛЬ_ПРЕПОДАЕТ_ПРЕДМЕТЫ_В_ГРУППАХ teacher_sub
left join ПРЕПОДАВАТЕЛЬ teacher
	on teacher_sub.ЛичныйНомер = teacher.ЛичныйНомер
where teacher_sub.НомерАудитории = 210

/*  9   */
select sub.НазваниеПредмета, gr.НазваниеГруппы
	from ПРЕПОДАВАТЕЛЬ_ПРЕПОДАЕТ_ПРЕДМЕТЫ_В_ГРУППАХ teacher_sub
left join СТУДЕНЧЕСКАЯ_ГРУППА gr
	on teacher_sub.КодовыйНомерГруппы = gr.КодовыйНомерГруппы
left join ПРЕДМЕТ sub
	on teacher_sub.КодовыйНомерПредмета = sub.КодовыйНомерПредмета
where 99 < teacher_sub.НомерАудитории and teacher_sub.НомерАудитории < 201

/*  10   */

select t1.НазваниеГруппы, t2.НазваниеГруппы from СТУДЕНЧЕСКАЯ_ГРУППА t1
join СТУДЕНЧЕСКАЯ_ГРУППА t2
on t1.Специальность = t2.Специальность
where t1.НазваниеГруппы <> t2.НазваниеГруппы

/*  11   */
select sum(КоличествоЧеловек) from СТУДЕНЧЕСКАЯ_ГРУППА
where Специальность = 'ЭВМ'

/*  12   */
select distinct ЛичныйНомер 
	from ПРЕПОДАВАТЕЛЬ_ПРЕПОДАЕТ_ПРЕДМЕТЫ_В_ГРУППАХ teacher_sub
left join СТУДЕНЧЕСКАЯ_ГРУППА gr
	on teacher_sub.КодовыйНомерГруппы = gr.КодовыйНомерГруппы
where gr.Специальность = 'ЭВМ'

/*  13  */

select КодовыйНомерПредмета from ПРЕПОДАВАТЕЛЬ_ПРЕПОДАЕТ_ПРЕДМЕТЫ_В_ГРУППАХ
group by КодовыйНомерПредмета
having count(*) in (select count(*) from ПРЕДМЕТ)

/*  14   */

with aim_teachers as (
	select distinct ЛичныйНомер from ПРЕПОДАВАТЕЛЬ_ПРЕПОДАЕТ_ПРЕДМЕТЫ_В_ГРУППАХ 
	where КодовыйНомерПредмета = '14П'
), aim_subj as (
	select distinct КодовыйНомерПредмета from ПРЕПОДАВАТЕЛЬ_ПРЕПОДАЕТ_ПРЕДМЕТЫ_В_ГРУППАХ
	where ЛичныйНомер in (select * from aim_teachers)
), ans_teachers_nums as (
	select distinct ЛичныйНомер from ПРЕПОДАВАТЕЛЬ_ПРЕПОДАЕТ_ПРЕДМЕТЫ_В_ГРУППАХ 
	where КодовыйНомерПредмета in (select * from aim_subj)
)

select Фамилия from ПРЕПОДАВАТЕЛЬ
where ЛичныйНомер in (select * from ans_teachers_nums)

/*  15   */

with aim_subj as (
	select distinct КодовыйНомерПредмета from ПРЕПОДАВАТЕЛЬ_ПРЕПОДАЕТ_ПРЕДМЕТЫ_В_ГРУППАХ 
	where ЛичныйНомер = '221Л'
)

select КодовыйНомерПредмета from ПРЕДМЕТ
except select КодовыйНомерПредмета from aim_subj

/*  16   */

with aim_subj as (
	select distinct КодовыйНомерПредмета from ПРЕПОДАВАТЕЛЬ_ПРЕПОДАЕТ_ПРЕДМЕТЫ_В_ГРУППАХ 
	where КодовыйНомерГруппы in (select КодовыйНомерГруппы from СТУДЕНЧЕСКАЯ_ГРУППА where НазваниеГруппы = 'М-6')
)

select КодовыйНомерПредмета from ПРЕДМЕТ
except select КодовыйНомерПредмета from aim_subj

/*  17   */

with aim_teacher_nums as (
	select distinct ЛичныйНомер from ПРЕПОДАВАТЕЛЬ_ПРЕПОДАЕТ_ПРЕДМЕТЫ_В_ГРУППАХ 
	where КодовыйНомерГруппы in ('3Г', '8Г')
)

select * from ПРЕПОДАВАТЕЛЬ
where ЛичныйНомер in (select * from aim_teacher_nums) and Должность = 'Доцент'

/*  18   */

with aim_teacher_nums as (
	select distinct ЛичныйНомер from ПРЕПОДАВАТЕЛЬ 
	where Кафедра = 'ЭВМ' and 'АСОИ' = any (Специальность)
)

select КодовыйНомерПредмета, ЛичныйНомер, КодовыйНомерГруппы from ПРЕПОДАВАТЕЛЬ_ПРЕПОДАЕТ_ПРЕДМЕТЫ_В_ГРУППАХ
where ЛичныйНомер in (select * from aim_teacher_nums)

/*  19   */

select distinct teacher_gr.КодовыйНомерГруппы from ПРЕПОДАВАТЕЛЬ_ПРЕПОДАЕТ_ПРЕДМЕТЫ_В_ГРУППАХ teacher_gr
left join ПРЕПОДАВАТЕЛЬ teacher on teacher.ЛичныйНомер = teacher_gr.ЛичныйНомер
left join СТУДЕНЧЕСКАЯ_ГРУППА gr on gr.КодовыйНомерГруппы = teacher_gr.КодовыйНомерГруппы
where gr.Специальность = any (teacher.Специальность) 

/*  20   */

with aim_teacher as (
	select ЛичныйНомер from ПРЕПОДАВАТЕЛЬ
	where Кафедра = 'ЭВМ'
)

select distinct teacher_gr.КодовыйНомерГруппы from ПРЕПОДАВАТЕЛЬ_ПРЕПОДАЕТ_ПРЕДМЕТЫ_В_ГРУППАХ teacher_gr
left join ПРЕПОДАВАТЕЛЬ teacher on teacher.ЛичныйНомер = teacher_gr.ЛичныйНомер
left join СТУДЕНЧЕСКАЯ_ГРУППА gr on gr.КодовыйНомерГруппы = teacher_gr.КодовыйНомерГруппы
where gr.Специальность = any (teacher.Специальность) and teacher_gr.ЛичныйНомер in (select * from aim_teacher)

/*  21   */

with aim_teacher as (
	select ЛичныйНомер from ПРЕПОДАВАТЕЛЬ
	where Кафедра = 'АСУ'
), aim_groups as (
	select distinct КодовыйНомерГруппы from ПРЕПОДАВАТЕЛЬ_ПРЕПОДАЕТ_ПРЕДМЕТЫ_В_ГРУППАХ
	where ЛичныйНомер in (select * from aim_teacher)
) 	

select distinct Специальность from СТУДЕНЧЕСКАЯ_ГРУППА
where КодовыйНомерГруппы in (select * from aim_groups)

/*  22   */

with aim_group_num as (
	select КодовыйНомерГруппы from СТУДЕНЧЕСКАЯ_ГРУППА
	where НазваниеГруппы = 'АС-8'
)

select КодовыйНомерПредмета from ПРЕПОДАВАТЕЛЬ_ПРЕПОДАЕТ_ПРЕДМЕТЫ_В_ГРУППАХ
where КодовыйНомерГруппы in (select * from aim_group_num)

/*  23   */

with aim_group_num as (
	select КодовыйНомерГруппы from СТУДЕНЧЕСКАЯ_ГРУППА
	where НазваниеГруппы = 'АС-8'
), aim_sub_nums as (
	select КодовыйНомерПредмета from ПРЕПОДАВАТЕЛЬ_ПРЕПОДАЕТ_ПРЕДМЕТЫ_В_ГРУППАХ
	where КодовыйНомерГруппы in (select * from aim_group_num)
)

select distinct КодовыйНомерГруппы from ПРЕПОДАВАТЕЛЬ_ПРЕПОДАЕТ_ПРЕДМЕТЫ_В_ГРУППАХ
where КодовыйНомерПредмета in (select * from aim_sub_nums)

/*  24   */
with used_subjects as (
	select КодовыйНомерПредмета from ПРЕПОДАВАТЕЛЬ_ПРЕПОДАЕТ_ПРЕДМЕТЫ_В_ГРУППАХ
	where КодовыйНомерГруппы in (
		select КодовыйНомерГруппы from СТУДЕНЧЕСКАЯ_ГРУППА where НазваниеГруппы = 'АС-8'
	) 
), not_aim_groups as (
	select distinct КодовыйНомерГруппы from ПРЕПОДАВАТЕЛЬ_ПРЕПОДАЕТ_ПРЕДМЕТЫ_В_ГРУППАХ
	where КодовыйНомерПредмета in (select * from used_subjects)
)

select КодовыйНомерГруппы from СТУДЕНЧЕСКАЯ_ГРУППА
except select КодовыйНомерГруппы from not_aim_groups

/*  25   */

with not_aim_subjects as (
	select КодовыйНомерПредмета from ПРЕПОДАВАТЕЛЬ_ПРЕПОДАЕТ_ПРЕДМЕТЫ_В_ГРУППАХ 
	where ЛичныйНомер = '430Л'
), not_aim_groups as (
	select distinct КодовыйНомерГруппы from ПРЕПОДАВАТЕЛЬ_ПРЕПОДАЕТ_ПРЕДМЕТЫ_В_ГРУППАХ 
	where КодовыйНомерПредмета in (select * from not_aim_subjects)
)

select КодовыйНомерГруппы from СТУДЕНЧЕСКАЯ_ГРУППА
except select КодовыйНомерГруппы from not_aim_groups

/*  26   */

with teachers as (
	select distinct ЛичныйНомер from ПРЕПОДАВАТЕЛЬ_ПРЕПОДАЕТ_ПРЕДМЕТЫ_В_ГРУППАХ
	where КодовыйНомерГруппы in (select КодовыйНомерГруппы from СТУДЕНЧЕСКАЯ_ГРУППА where НазваниеГруппы = 'Э-15')
), not_aim_teachers as (
	select distinct ЛичныйНомер from ПРЕПОДАВАТЕЛЬ_ПРЕПОДАЕТ_ПРЕДМЕТЫ_В_ГРУППАХ
	where КодовыйНомерПредмета = '12П'
)

select * from teachers
except select * from not_aim_teachers


