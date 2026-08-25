create database python;

-- drop database python;
 
use python;

create table processador (
	id int primary key auto_increment,
    processador_uso decimal(4,1),
    processador_freq int,
    dt_captura datetime
);
    
create table ram(
	id int primary key auto_increment,
    ram_uso decimal(4,1),
    dt_captura datetime
);

create table disco (
	id int primary key auto_increment,
    disco_uso decimal(4,1),
    dt_captura datetime
   
);

select * from processador;

truncate table processador;

