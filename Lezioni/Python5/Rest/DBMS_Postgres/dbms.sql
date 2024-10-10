create table Cittadini (
    nome varchar not null
    cognome varchar not null
    dataNascita date not null
    codFiscale varchar not null
    primary key (codFiscale)
);

create table Utenti (
    username varchar not null
    password varchar not null
    id serial not null
    admin boolean
    primary key (id)
);