
insert into ПРЕПОДАВАТЕЛЬ (ЛичныйНомер, Фамилия, Должность, Кафедра, Специальность, ТелефонДомашний)
values ('221Л', 'Фролов', 'Доцент', 'ЭВМ', '{"АСОИ", "ЭВМ"}', '487'),
       ('222Л', 'Костин', 'Доцент', 'ЭВМ', '{"ЭВМ"}', '543'),
       ('225Л', 'Бойко', 'Профессор', 'АСУ', '{"АСОИ", "ЭВМ"}', '112'),
       ('430Л', 'Глазов', 'Ассистент', 'ТФ', '{"СД"}', '421'),
       ('110Л', 'Петров', 'Ассистент', 'Экономики', '{"Международная экономика"}', '324');

insert into ПРЕДМЕТ (КодовыйНомерПредмета, НазваниеПредмета, КоличествоЧасов, Специальность, Семестр)
values ('12П', 'Мини ЭВМ', '36', 'ЭВМ', '1'),
       ('14П', 'ПЭВМ', '72', 'ЭВМ', '1'),
       ('17П', 'СУБД ПК', '48', 'АСОИ', '4'),
       ('18П', 'ВКСС', '52', 'АСОИ', '6'),
       ('34П', 'Физика', '30', 'СД', '6'),
       ('22П', 'Аудит', '24', 'Бухучет', '3');

insert into СТУДЕНЧЕСКАЯ_ГРУППА (КодовыйНомерГруппы, НазваниеГруппы, КоличествоЧеловек, Специальность, ФамилияСтаросты)
values ('8Г', 'Э-12', '18', 'ЭВМ', 'Иванова'),
       ('7Г', 'Э-15', '22', 'ЭВМ', 'Сеткин'),
       ('4Г', 'АС-9', '24', 'АСОИ', 'Балабанов'),
       ('3Г', 'АС-8', '20', 'АСОИ', 'Чижов'),
       ('17Г', 'С-14', '29', 'СД', 'Амросов'),
       ('12Г', 'М-6', '16', 'Международная экономика', 'Трубин'),
       ('10Г', 'Б-4', '21', 'Бухучет', 'Зязюткин');

insert into ПРЕПОДАВАТЕЛЬ_ПРЕПОДАЕТ_ПРЕДМЕТЫ_В_ГРУППАХ (КодовыйНомерГруппы, КодовыйНомерПредмета, ЛичныйНомер, НомерАудитории)
values ('8Г', '12П', '222Л', '112'),
       ('8Г', '14П', '221Л', '220'),
       ('8Г', '17П', '222Л', '112'),
       ('7Г', '14П', '221Л', '220'),
       ('7Г', '17П', '222Л', '241'),
       ('7Г', '18П', '225Л', '210'),
       ('4Г', '12П', '222Л', '112'),
       ('4Г', '18П', '225Л', '210'),
       ('3Г', '12П', '222Л', '112'),
       ('3Г', '17П', '221Л', '241'),
       ('3Г', '18П', '225Л', '210'),
       ('17Г', '12П', '222Л', '112'),
       ('17Г', '22П', '110Л', '220'),
       ('17Г', '34П', '430Л', '118'),
       ('12Г', '12П', '222Л', '112'),
       ('12Г', '22П', '110Л', '210'),
       ('10Г', '12П', '222Л', '210'),
       ('10Г', '22П', '110Л', '210');