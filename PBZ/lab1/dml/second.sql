/* 16. Получить общее количество деталей Д1, поставляемых поставщиком П1. */

select sum(s) from Количество_Деталей
where П = 'П1' and Д = 'Д1'

/* 27. Получить номера поставщиков, поставляющих деталь Д1 для некоторого проекта в количестве,
большем среднего количества деталей Д1 в поставках для этого проекта. */

with avg_count as (
	select ПР, avg(s) averege from Количество_Деталей
	where Д = 'Д1'
	group by ПР	
)

select d_count.П, d_count.ПР, d_count.s, avg_count.averege 
	from Количество_Деталей d_count
left join avg_count
	on d_count.ПР = avg_count.ПР
where Д = 'Д1' and d_count.s > avg_count.averege

/* 35. Получить пары "номер поставщика-номер детали", такие, что данный поставщик не поставляет
данную деталь. */

with 
    cross_joined as (
        select Детали_p.Д, Поставщики_s.П from Детали_p cross join Поставщики_s
    ),
    not_aim_pairs as (
        select distinct d_count.П, d_count.Д
            from Количество_Деталей d_count
        order by d_count.П, d_count.Д
    )

select П, Д from cross_joined
except select П, Д from not_aim_pairs
order by П, Д

/* 5. Получить все сочетания "цвета деталей-города деталей". */

select distinct Цвет, Город from Детали_p

/* 8. Получить все такие тройки "номера поставщиков-номера деталей-номера проектов", для которых
никакие из двух выводимых поставщиков, деталей и проектов не размещены в одном городе. */

select d_count.П, d_count.Д, d_count.ПР from Количество_Деталей d_count
left join Поставщики_s dillers
	on d_count.П = dillers.П
left join Детали_p d
	on d_count.Д = d.Д
left join Проекты_j pr
	on d_count.ПР = pr.ПР
where dillers.Город <> d.Город and dillers.Город <> pr.Город and pr.Город <> d.Город

/* 17. Для каждой детали, поставляемой для проекта, получить номер детали, номер проекта и
соответствующее общее количество. */

select Д, ПР, sum(s) from Количество_Деталей
group by Д, ПР
order by Д, ПР

/* 21. Получить номера деталей, поставляемых для какого-либо проекта в Лондоне. */

select distinct d_count.Д from Количество_Деталей d_count
left join Проекты_j pr
on d_count.ПР = pr.ПР
where pr.Город = 'Москва'

/* 12. Получить номера деталей, поставляемых для всех проектов, обеспечиваемых поставщиком из
того же города, где размещен проект. */

select d_count.Д from Количество_Деталей d_count
left join Проекты_j pr
	on d_count.ПР = pr.ПР
left join Поставщики_s dillers
	on d_count.П = dillers.П
where dillers.Город = pr.Город

/* 29. Получить номера проектов, полностью обеспечиваемых поставщиком П1. */

select ПР from Количество_Деталей
group by ПР 
having string_agg(П, '') = 'П1'

/* 23. Получить номера поставщиков, поставляющих по крайней мере одну деталь, поставляемую по
крайней мере одним поставщиком, который поставляет по крайней мере одну красную деталь. */

with 
	dillers_with_red_details as (
		select distinct d_count.П П from Количество_Деталей d_count
		left join Детали_p d
		on d_count.Д = d.Д
		where d.Цвет = 'Красный'
	),
	aim_details as (
		select distinct d_count.Д Д from Количество_Деталей d_count
		where d_count.П in (select П from dillers_with_red_details)
	)
	
select distinct d_count.П from Количество_Деталей d_count
where d_count.Д in (select Д from aim_details)