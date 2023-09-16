create type ГородEnum as enum ('Москва', 'Таллинн', 'Минск', 'Киев', 'Вильнюс', 'Псков', 'Саратов');
create type ЦветEnum as enum ('Красный', 'Зеленая', 'Черный');


create table Поставщики_S
(
    П      varchar(2) primary key,
    ИмяП   varchar(10) not null,
    Статус SMALLSERIAL not null,
    Город  ГородEnum   not null
);

create table Детали_P
(
    Д      varchar(2) primary key,
    ИмяД   varchar(10) not null,
    Цвет   ЦветEnum    not null,
    Размер SMALLSERIAL not null,
    Город  ГородEnum
);

create table Проекты_J
(
    ПР    varchar(50) primary key,
    ИмяПР varchar(4) not null,
    Город ГородEnum  not null
);

create table Количество_Деталей
(
    П  varchar(50),
    Д  varchar(50),
    ПР varchar(50),
    S  integer,

    primary key (П, Д, ПР),

    foreign key (П) references Поставщики_S (П),
    foreign key (Д) references Детали_P (Д),
    foreign key (ПР) references Проекты_J (ПР)
);