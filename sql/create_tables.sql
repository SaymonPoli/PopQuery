CREATE TABLE Funcionario (
    id_funcionario SERIAL PRIMARY KEY,
    Nome VARCHAR(255) NOT NULL
);

CREATE TABLE Cliente (
    id_cliente SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    contato VARCHAR(255)
);

CREATE TABLE Bomboniere (
    id_item SERIAL PRIMARY KEY,
    descricao VARCHAR(255) NOT NULL,
    valor_uni DECIMAL(10, 2) NOT NULL CHECK (valor_uni >= 0)
);

CREATE TABLE Sala (
    numero_sala SERIAL PRIMARY KEY,
    lotacao INT NOT NULL CHECK (lotacao > 0)
);

CREATE TABLE Genero (
    id_genero SERIAL PRIMARY KEY,
    descricao VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE Diretor (
    id_diretor SERIAL PRIMARY KEY,
    nome_diretor VARCHAR(255) NOT NULL
);

CREATE TABLE Ator (
    id_ator SERIAL PRIMARY KEY,
    nome_ator VARCHAR(255) NOT NULL
);

-- -----------------------------------------------------
-- GRUPO 2: Tabelas com dependências de Nível 1
-- -----------------------------------------------------

CREATE TABLE Assento (
    id_assento SERIAL PRIMARY KEY,
    linha VARCHAR(5) NOT NULL,
    coluna VARCHAR(5) NOT NULL,
    vip BOOLEAN DEFAULT FALSE,
    fk_numero_sala INT NOT NULL,
    
    FOREIGN KEY (fk_numero_sala) REFERENCES Sala(numero_sala) ON DELETE CASCADE
);

CREATE TABLE Filme (
    id_filme SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    sinopse TEXT,
    faixa_etaria VARCHAR(10),
    nota_imdb FLOAT,
    data_inicio DATE NOT NULL,
    data_fim DATE NOT NULL,
    fk_id_genero INT NOT NULL,
    fk_id_diretor INT,

    FOREIGN KEY (fk_id_genero) REFERENCES Genero(id_genero) ON DELETE RESTRICT,
    FOREIGN KEY (fk_id_diretor) REFERENCES Diretor(id_diretor) ON DELETE SET NULL
);

-- -----------------------------------------------------
-- GRUPO 3: Tabelas com dependências de Nível 2
-- -----------------------------------------------------

CREATE TABLE Sessao (
    id_sessao SERIAL PRIMARY KEY,
    horario TIME NOT NULL,
    data DATE NOT NULL,
    eh_3d BOOLEAN DEFAULT FALSE, 
    fk_numero_sala INT NOT NULL,
    fk_id_filme INT NOT NULL,
    
    FOREIGN KEY (fk_numero_sala) REFERENCES Sala(numero_sala) ON DELETE RESTRICT,
    FOREIGN KEY (fk_id_filme) REFERENCES Filme(id_filme) ON DELETE CASCADE
);

CREATE TABLE Ingresso (
    id_ingresso SERIAL PRIMARY KEY,
    valor DECIMAL(10, 2) NOT NULL,
    meia_entrada BOOLEAN DEFAULT FALSE,
    fk_id_sessao INT NOT NULL,
    
    FOREIGN KEY (fk_id_sessao) REFERENCES Sessao(id_sessao) ON DELETE CASCADE
);

-- -----------------------------------------------------
-- GRUPO 4: Tabelas Associativas (Relacionamentos N:M)
-- -----------------------------------------------------

CREATE TABLE Venda (
    id_venda SERIAL PRIMARY KEY,
    data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    valor DECIMAL(10, 2) NOT NULL, 
    fk_id_funcionario INT, 
    fk_id_cliente INT, 
    fk_id_item INT NOT NULL, 
    
    FOREIGN KEY (fk_id_funcionario) REFERENCES Funcionario(id_funcionario) ON DELETE SET NULL,
    FOREIGN KEY (fk_id_cliente) REFERENCES Cliente(id_cliente) ON DELETE SET NULL,
    FOREIGN KEY (fk_id_item) REFERENCES Bomboniere(id_item) ON DELETE RESTRICT
);

CREATE TABLE elenco (
    fk_id_filme INT NOT NULL,
    fk_id_ator INT NOT NULL,
    
    PRIMARY KEY (fk_id_filme, fk_id_ator),
    
    FOREIGN KEY (fk_id_filme) REFERENCES Filme(id_filme) ON DELETE CASCADE,
    FOREIGN KEY (fk_id_ator) REFERENCES Ator(id_ator) ON DELETE CASCADE
);

CREATE TABLE Cliente_Ingresso (
    fk_id_cliente INT NOT NULL,
    fk_id_ingresso INT NOT NULL,
    quantidade INT NOT NULL CHECK (quantidade > 0),
    valor_total DECIMAL(10, 2) NOT NULL,
    data_emissao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_nota VARCHAR(255), 
    
    PRIMARY KEY (fk_id_cliente, fk_id_ingresso),
    FOREIGN KEY (fk_id_cliente) REFERENCES Cliente(id_cliente) ON DELETE CASCADE,
    FOREIGN KEY (fk_id_ingresso) REFERENCES Ingresso(id_ingresso) ON DELETE CASCADE
);

CREATE TABLE assento_ingresso (
    fk_id_assento INT NOT NULL,
    fk_id_ingresso INT NOT NULL,
    
    PRIMARY KEY (fk_id_assento, fk_id_ingresso),
    FOREIGN KEY (fk_id_assento) REFERENCES Assento(id_assento) ON DELETE CASCADE,
    FOREIGN KEY (fk_id_ingresso) REFERENCES Ingresso(id_ingresso) ON DELETE CASCADE
);

CREATE OR REPLACE FUNCTION validar_periodo_sessao()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.data < (SELECT data_inicio FROM Filme WHERE id_filme = NEW.fk_id_filme)
       OR NEW.data > (SELECT data_fim FROM Filme WHERE id_filme = NEW.fk_id_filme) THEN
        RAISE EXCEPTION 'A sessão está fora do período de exibição do filme.';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER tg_validar_periodo_sessao
BEFORE INSERT OR UPDATE ON Sessao
FOR EACH ROW EXECUTE FUNCTION validar_periodo_sessao();
