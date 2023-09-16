create type ДолжностьEnum as emum ('Доцент', 'Профессор', 'Ассистент');
create type КафедраEnum as enum ('ЭВМ', 'АСУ', 'ТФ', 'Экономики');
create type СпециальностьEnum as emum ('АСОИ', 'ЭВМ', 'СД', 'Международная экономика', 'Бухучет');

create table ПРЕПОДАВАТЕЛЬ
(
    ЛичныйНомер     varchar(4) primary key,
    Фамилия         varchar(10)         not null,
    Должность       ДолжностьEnum       not null,
    Кафедра         КафедраEnum         not null,
    Специальность   СпециальностьEnum[] not null,
    ТелефонДомашний varchar(3)          not null
);

create table ПРЕДМЕТ
(
    КодовыйНомерПредмета varchar(3) primary key,
    НазваниеПредмета     varchar(10)       not null,
    КоличествоЧасов      smallserial       not null,
    Специальность        СпециальностьEnum not null,
    Семестр              smallserial       not null
);


create table СТУДЕНЧЕСКАЯ_ГРУППА
(
    КодовыйНомерГруппы varchar(4) primary key,
    НазваниеГруппы     varchar(5)        not null,
    КоличествоЧеловек  SERIAL            not null,
    Специальность      СпециальностьEnum not null,
    ФамилияСтаросты    varchar(10)       not null
);

create table ПРЕПОДАВАТЕЛЬ_ПРЕПОДАЕТ_ПРЕДМЕТЫ_В_ГРУППАХ
(
    КодовыйНомерГруппы   varchar(4)  not null,
    КодовыйНомерПредмета varchar(3)  not null,
    ЛичныйНомер          varchar(4)  not null,
    НомерАудитории       smallserial not null,

    primary key (КодовыйНомерГруппы, КодовыйНомерПредмета, ЛичныйНомер),

    foreign key (КодовыйНомерГруппы) references СТУДЕНЧЕСКАЯ_ГРУППА (КодовыйНомерГруппы),
    foreign key (КодовыйНомерПредмета) references ПРЕДМЕТ (КодовыйНомерПредмета),
    foreign key (ЛичныйНомер) references ПРЕПОДАВАТЕЛЬ (ЛичныйНомер)
);
