create table IF NOT EXISTS LmsUser (
    UserName nvarchar(256) not null,
    constraint PK_LmsUser primary key (UserName),
    constraint UN_UserName unique (UserName)
);

create table IF NOT EXISTS Book (
	BookID int not null auto_increment,
    ISBN text not null,
    Title text not null,
    Author text not null,
    constraint PK_Book primary key (BookID)
);

create table IF NOT EXISTS BookBorrowed (
	BookBorrowedID int not null auto_increment,
    UserName nvarchar(256) not null,
    BookID int not null,
    Status enum ('borrowed', 'returned'),
    BorrowedDate date not null,
    ReturnedDate date null,
    constraint PK_BookBorrowed primary key (BookBorrowedID),
    constraint FK_BookBorrowed_LmsUser foreign key (UserName) references LmsUser (UserName),
    constraint FK_BookBorrowed_Book foreign key (BookID) references Book (BookID)
);