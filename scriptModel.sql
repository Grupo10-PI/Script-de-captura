create database grupo10;

-- drop database grupo10;

use grupo10;

create table maquina (
	id int primary key auto_increment,
    nome varchar(45) not null,
    nucleosFisicos int,
    nucleosLogicos int,
    capacidadeTotal bigint,
    ramTotal bigint,
    dtCadastro datetime
);

-- create table componentes (
-- 	id int primary key auto_increment,
--     nome varchar(45),
--     tipo varchar(45)
-- );

create table registros (
	idRegistro int auto_increment,
  --  fkComponente int,
    fkMaquina int,
    cpuPorcentagemUso decimal (4,1),
    cpuFrequenciaAtual int,
    cpuUsoPorNucleo int, 
    cpuTemperatura Decimal (5,2),
    ramDisponivel int,
    ramUsada int,
    ramPercentualUso decimal(4,1),
    discoEspacoUsado int,
    discoEspacoLivre int,
    dtRegistro datetime,
	constraint pkComposta primary key (idRegistro, fkMaquina),
--   constraint fkComponenteRegistro foreign key (fkComponente) references componentes(id),
    constraint fkMaquinaRegistro foreign key (fkMaquina) references maquina(id)
);

select * from maquina;
SELECT nome FROM maquina WHERE id = 1;

select * from registros;
-- select * from componentes;


    