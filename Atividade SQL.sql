USE CARAMELO;


CREATE TABLE tb_clientes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome_cliente VARCHAR(150),
    data_nascimento DATE,
    sexo VARCHAR(20),
    email VARCHAR(100),
    telefone VARCHAR(50),
    cidade VARCHAR(50),
    estado VARCHAR(2),
    data_cadastro DATE);


CREATE TABLE tb_produtos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome_produto VARCHAR(300),
    categoria VARCHAR(100),
    subcategoria VARCHAR(100),
    marca VARCHAR(100),
    preco_unitario DECIMAL(10,2));


CREATE TABLE tb_vendas (
    id_venda INT PRIMARY KEY,
    data_venda DATE,
    id_cliente INT,
    id_produto INT,
    quantidade INT,
    forma_pagamento VARCHAR(40),
    canal_venda VARCHAR(40),
    FOREIGN KEY (id_cliente) REFERENCES tb_clientes(id),
    FOREIGN KEY (id_produto) REFERENCES tb_produtos(id));






SET GLOBAL local_infile = 1;






LOAD DATA INFILE 'C:/Users/cassio.pereira/Documents/Repo_Senac/tb_clientebi.csv'
INTO TABLE tb_clientes
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(nome_cliente, data_nascimento, sexo, email, telefone, cidade, estado,data_cadastro);


LOAD DATA INFILE 'C:/Users/cassio.pereira/Documents/Repo_Senac/tb_produtos.csv'
INTO TABLE tb_produtos
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(nome_produto, categoria, subcategoria, marca, preco_unitario);

LOAD DATA INFILE 'C:/Users/cassio.pereira/Documents/Repo_Senac/tb_vendas.csv'
INTO TABLE tb_vendas
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;






drop table tb_produtos;

drop table tb_vendas;

drop table tb_clientes;

select * from tb_produtos;

select * from tb_clientes;

select * from tb_vendas;