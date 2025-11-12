/* TrabalhoFinal_log: */

CREATE TABLE Funcionario (
    Nome VARCHAR,
    id_funcionario INTEGER PRIMARY KEY
);

CREATE TABLE Bomboniere (
    id_item INTEGER PRIMARY KEY,
    descricao VARCHAR,
    valor_uni FLOAT
);

CREATE TABLE Cliente (
    id_cliente INTEGER PRIMARY KEY,
    nome VARCHAR,
    contato VARCHAR
);

CREATE TABLE Ingresso (
    id_ingresso INTEGER PRIMARY KEY,
    valor FLOAT,
    fk__Sessao_id_sessao INTEGER,
    meia_entrada BOOLEAN
);

CREATE TABLE Assento (
    id_assento INTEGER PRIMARY KEY,
    linha VARCHAR,
    coluna VARCHAR,
    vip BOOLEAN,
    fk_Sala_numero_sala INTEGER
);

CREATE TABLE Sala (
    numero_sala INTEGER PRIMARY KEY,
    lotacao VARCHAR
);

CREATE TABLE Genero (
    id_genero INTEGER PRIMARY KEY,
    descricao VARCHAR
);

CREATE TABLE ator (
    id_ator INTEGER PRIMARY KEY,
    nome_ator VARCHAR
);

CREATE TABLE Diretor (
    id_diretor INTEGER PRIMARY KEY,
    nome_diretor VARCHAR
);

CREATE TABLE Filme (
    id_filme INTEGER PRIMARY KEY,
    nome VARCHAR,
    sinopse VARCHAR,
    faixa_etaria INTEGER,
    nota_imdb FLOAT,
    fk_Genero_id_genero INTEGER,
    fk_Diretor_id_diretor INTEGER
);

CREATE TABLE _Sessao (
    id_sessao INTEGER PRIMARY KEY,
    horario TIME,
    data DATE,
    3d BOOLEAN,
    fk_Sala_numero_sala INTEGER,
    fk_Filme_id_filme INTEGER
);

CREATE TABLE Venda_Funcionario_Cliente_Bomboniere (
    fk_Funcionario_id_funcionario INTEGER,
    fk_Cliente_id_cliente INTEGER,
    fk_Bomboniere_id_item INTEGER
);

CREATE TABLE Cliente_Ingresso (
    fk_Ingresso_id_ingresso INTEGER,
    fk_Cliente_id_cliente INTEGER,
    valor_total FLOAT,
    id_nota INTEGER PRIMARY KEY,
    quantidade INTEGER,
    data_emissao DATE
);

CREATE TABLE assento_ingresso (
    fk_Ingresso_id_ingresso INTEGER,
    fk_Assento_id_assento INTEGER
);

CREATE TABLE elenco (
    fk_ator_id_ator INTEGER,
    fk_Filme_id_filme INTEGER
);
 
ALTER TABLE Ingresso ADD CONSTRAINT FK_Ingresso_2
    FOREIGN KEY (fk__Sessao_id_sessao)
    REFERENCES _Sessao (id_sessao)
    ON DELETE RESTRICT;
 
ALTER TABLE Assento ADD CONSTRAINT FK_Assento_2
    FOREIGN KEY (fk_Sala_numero_sala)
    REFERENCES Sala (numero_sala)
    ON DELETE CASCADE;
 
ALTER TABLE Filme ADD CONSTRAINT FK_Filme_2
    FOREIGN KEY (fk_Genero_id_genero)
    REFERENCES Genero (id_genero)
    ON DELETE CASCADE;
 
ALTER TABLE Filme ADD CONSTRAINT FK_Filme_3
    FOREIGN KEY (fk_Diretor_id_diretor)
    REFERENCES Diretor (id_diretor)
    ON DELETE CASCADE;
 
ALTER TABLE _Sessao ADD CONSTRAINT FK__Sessao_2
    FOREIGN KEY (fk_Sala_numero_sala)
    REFERENCES Sala (numero_sala);
 
ALTER TABLE _Sessao ADD CONSTRAINT FK__Sessao_3
    FOREIGN KEY (fk_Filme_id_filme)
    REFERENCES Filme (id_filme);
 
ALTER TABLE Venda_Funcionario_Cliente_Bomboniere ADD CONSTRAINT FK_Venda_Funcionario_Cliente_Bomboniere_1
    FOREIGN KEY (fk_Funcionario_id_funcionario)
    REFERENCES Funcionario (id_funcionario)
    ON DELETE RESTRICT;
 
ALTER TABLE Venda_Funcionario_Cliente_Bomboniere ADD CONSTRAINT FK_Venda_Funcionario_Cliente_Bomboniere_2
    FOREIGN KEY (fk_Cliente_id_cliente)
    REFERENCES Cliente (id_cliente)
    ON DELETE NO ACTION;
 
ALTER TABLE Venda_Funcionario_Cliente_Bomboniere ADD CONSTRAINT FK_Venda_Funcionario_Cliente_Bomboniere_3
    FOREIGN KEY (fk_Bomboniere_id_item)
    REFERENCES Bomboniere (id_item)
    ON DELETE NO ACTION;
 
ALTER TABLE Cliente_Ingresso ADD CONSTRAINT FK_Cliente_Ingresso_2
    FOREIGN KEY (fk_Ingresso_id_ingresso)
    REFERENCES Ingresso (id_ingresso)
    ON DELETE SET NULL;
 
ALTER TABLE Cliente_Ingresso ADD CONSTRAINT FK_Cliente_Ingresso_3
    FOREIGN KEY (fk_Cliente_id_cliente)
    REFERENCES Cliente (id_cliente)
    ON DELETE SET NULL;
 
ALTER TABLE assento_ingresso ADD CONSTRAINT FK_assento_ingresso_1
    FOREIGN KEY (fk_Ingresso_id_ingresso)
    REFERENCES Ingresso (id_ingresso)
    ON DELETE RESTRICT;
 
ALTER TABLE assento_ingresso ADD CONSTRAINT FK_assento_ingresso_2
    FOREIGN KEY (fk_Assento_id_assento)
    REFERENCES Assento (id_assento)
    ON DELETE SET NULL;
 
ALTER TABLE elenco ADD CONSTRAINT FK_elenco_1
    FOREIGN KEY (fk_ator_id_ator)
    REFERENCES ator (id_ator)
    ON DELETE RESTRICT;
 
ALTER TABLE elenco ADD CONSTRAINT FK_elenco_2
    FOREIGN KEY (fk_Filme_id_filme)
    REFERENCES Filme (id_filme)
    ON DELETE SET NULL;
