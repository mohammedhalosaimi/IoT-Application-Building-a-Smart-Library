create table IF NOT EXISTS Book(
    BookID int not null auto_increment,
    ISBN text not null,
    Title text not null,
    Author text not null,
    constraint PK_Book primary key (BookID)
);