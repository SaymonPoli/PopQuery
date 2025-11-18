DELETE FROM assento_ingresso;
DELETE FROM Cliente_Ingresso;
DELETE FROM elenco;
DELETE FROM Venda;
DELETE FROM Ingresso;
DELETE FROM Sessao;
DELETE FROM Filme;
DELETE FROM Assento;
DELETE FROM Ator;
DELETE FROM Diretor;
DELETE FROM Genero;
DELETE FROM Sala;
DELETE FROM Bomboniere;
DELETE FROM Cliente;
DELETE FROM Funcionario;

-- -----------------------------------------------------
-- PASSO 2: Inserir dados nas tabelas base
-- -----------------------------------------------------

-- Inserir Gêneros (10)
INSERT INTO Genero (id_genero, descricao) VALUES
(1, 'Ação'),
(2, 'Fantasia'),
(3, 'Romance'),
(4, 'Comédia'),
(5, 'Animação'),
(6, 'Crime'),
(7, 'Drama'),
(8, 'Ficção Científica'),
(9, 'Suspense'),
(10, 'Comédia Romântica');

-- Inserir Diretores (14)
INSERT INTO Diretor (id_diretor, nome_diretor) VALUES
(1, 'Peter Jackson'),
(2, 'Catherine Hardwicke'),
(3, 'Chris Weitz'),
(4, 'David Slade'),
(5, 'Bill Condon'),
(6, 'Gil Junger'),
(7, 'Justin Lin'),
(8, 'James Wan'),
(9, 'F. Gary Gray'),
(10, 'Andrew Adamson'),
(11, 'Francis Ford Coppola'),
(12, 'Orson Welles'),
(13, 'Stanley Kubrick'),
(14, 'Alfred Hitchcock'),
(15, 'Charlie Chaplin'),
(16, 'Quentin Tarantino'),
(17, 'Michael Curtiz');

-- Inserir Atores (26)
INSERT INTO Ator (id_ator, nome_ator) VALUES
(1, 'Elijah Wood'),
(2, 'Ian McKellen'),
(3, 'Viggo Mortensen'),
(4, 'Kristen Stewart'),
(5, 'Robert Pattinson'),
(6, 'Taylor Lautner'),
(7, 'Heath Ledger'),
(8, 'Julia Stiles'),
(9, 'Joseph Gordon-Levitt'),
(10, 'Vin Diesel'),
(11, 'Paul Walker'),
(12, 'Dwayne Johnson'),
(13, 'Jordana Brewster'),
(14, 'Mike Myers'),
(15, 'Eddie Murphy'),
(16, 'Cameron Diaz'),
(17, 'Marlon Brando'),
(18, 'Al Pacino'),
(19, 'Joseph Cotten'),
(20, 'Keir Dullea'),
(21, 'Anthony Perkins'),
(22, 'Charlie Chaplin'),
(23, 'Paulette Goddard'),
(24, 'John Travolta'),
(25, 'Uma Thurman'),
(26, 'Humphrey Bogart'),
(27, 'Ingrid Bergman');

-- Inserir Salas (3)
INSERT INTO Sala (numero_sala, lotacao) VALUES
(1, 150), -- Sala Comum
(2, 80),  -- Sala VIP
(3, 250); -- Sala IMAX

-- Inserir Clientes (20)
INSERT INTO Cliente (id_cliente, nome, contato) VALUES
(1, 'Ana Beatriz', 'ana.beatriz@email.com'),
(2, 'Bruno Costa', 'bruno.c@email.com'),
(3, 'Carla Dias', 'carla.dias@email.com'),
(4, 'Daniel Moreira', 'daniel.m@email.com'),
(5, 'Eduarda Lima', 'eduarda.lima@email.com'),
(6, 'Felipe Alves', 'felipe.a@email.com'),
(7, 'Gabriela Rocha', 'gabriela.r@email.com'),
(8, 'Heitor Martins', 'heitor.m@email.com'),
(9, 'Isabela Santos', 'isabela.s@email.com'),
(10, 'João Pedro', 'joao.pedro@email.com'),
(11, 'Karina Oliveira', 'karina.o@email.com'),
(12, 'Lucas Mendes', 'lucas.m@email.com'),
(13, 'Manuela Ferreira', 'manuela.f@email.com'),
(14, 'Nicolas Azevedo', 'nicolas.a@email.com'),
(15, 'Olivia Ribeiro', 'olivia.r@email.com'),
(16, 'Pedro Henrique', 'pedro.h@email.com'),
(17, 'Quintino Bessa', 'quintino.b@email.com'),
(18, 'Rafaela Nunes', 'rafaela.n@email.com'),
(19, 'Samuel Guedes', 'samuel.g@email.com'),
(20, 'Vitória Barros', 'vitoria.b@email.com');

-- Inserir Funcionários (2)
INSERT INTO Funcionario (id_funcionario, Nome) VALUES
(1, 'Marcos Atendente'),
(2, 'Juliana Gerente');

-- Inserir Itens da Bomboniere (3)
INSERT INTO Bomboniere (id_item, descricao, valor_uni) VALUES
(1, 'Pipoca Grande (Salgada)', 25.00),
(2, 'Refrigerante 700ml', 15.00),
(3, 'Chocolate M&M', 12.00);

-- -----------------------------------------------------
-- PASSO 3: Inserir Filmes (30)
-- -----------------------------------------------------

-- Saga Senhor dos Anéis (3)
INSERT INTO Filme (id_filme, nome, sinopse, faixa_etaria, nota_imdb, fk_id_genero, fk_id_diretor) VALUES
(1, 'O Senhor dos Anéis: A Sociedade do Anel', 'Um jovem hobbit...', '12', 8.8, 2, 1),
(2, 'O Senhor dos Anéis: As Duas Torres', 'Enquanto Frodo e Sam...', '12', 8.8, 2, 1),
(3, 'O Senhor dos Anéis: O Retorno do Rei', 'A batalha final pela...', '12', 9.0, 2, 1);

-- 10 Coisas que Eu Odeio em Você (1)
INSERT INTO Filme (id_filme, nome, sinopse, faixa_etaria, nota_imdb, fk_id_genero, fk_id_diretor) VALUES
(4, '10 Coisas que Eu Odeio em Você', 'Um estudante novo...', '12', 7.3, 10, 6);

-- Saga Crepúsculo (5)
INSERT INTO Filme (id_filme, nome, sinopse, faixa_etaria, nota_imdb, fk_id_genero, fk_id_diretor) VALUES
(5, 'A Saga Crepúsculo: Crepúsculo', 'Bella Swan se muda...', '14', 5.3, 3, 2),
(6, 'A Saga Crepúsculo: Lua Nova', 'Edward deixa Bella...', '14', 4.7, 3, 3),
(7, 'A Saga Crepúsculo: Eclipse', 'Uma série de assassinatos...', '14', 5.0, 3, 4),
(8, 'A Saga Crepúsculo: Amanhecer - Parte 1', 'Bella e Edward se casam...', '14', 4.9, 3, 5),
(9, 'A Saga Crepúsculo: Amanhecer - Parte 2', 'Bella se ajusta à...', '14', 5.5, 3, 5);

-- Saga Velozes e Furiosos (10)
INSERT INTO Filme (id_filme, nome, sinopse, faixa_etaria, nota_imdb, fk_id_genero, fk_id_diretor) VALUES
(10, 'Velozes e Furiosos', 'Um policial disfarçado...', '14', 6.8, 1, 7),
(11, '+Velozes +Furiosos', 'Brian OConner está...', '14', 5.9, 1, 7),
(12, 'Velozes e Furiosos: Desafio em Tóquio', 'Um adolescente se...', '14', 6.0, 1, 7),
(13, 'Velozes e Furiosos 4', 'Brian OConner...', '14', 6.5, 1, 7),
(14, 'Velozes e Furiosos 5: Operação Rio', 'Dom e Brian...', '14', 7.3, 1, 7),
(15, 'Velozes e Furiosos 6', 'Dom e Brian...', '14', 7.0, 1, 7),
(16, 'Velozes e Furiosos 7', 'Após os eventos...', '14', 7.1, 1, 8),
(17, 'Velozes e Furiosos 8', 'Dom é seduzido...', '14', 6.6, 1, 9),
(18, 'Velozes e Furiosos 9', 'Dom Toretto...', '14', 5.2, 1, 7),
(19, 'Velozes e Furiosos 10', 'Dom Toretto e sua...', '14', 5.8, 1, 7);

-- Saga Shrek (4)
INSERT INTO Filme (id_filme, nome, sinopse, faixa_etaria, nota_imdb, fk_id_genero, fk_id_diretor) VALUES
(20, 'Shrek', 'Um ogro mal-humorado...', 'L', 7.9, 5, 10),
(21, 'Shrek 2', 'Shrek e Fiona...', 'L', 7.3, 5, 10),
(22, 'Shrek Terceiro', 'Quando o pai de Fiona...', 'L', 6.1, 5, 10),
(23, 'Shrek para Sempre', 'Shrek está entediado...', 'L', 6.3, 5, 10);

-- Clássicos (7)
INSERT INTO Filme (id_filme, nome, sinopse, faixa_etaria, nota_imdb, fk_id_genero, fk_id_diretor) VALUES
(24, 'O Poderoso Chefão', 'O patriarca de uma...', '16', 9.2, 6, 11),
(25, 'Cidadão Kane', 'Seguindo a morte de...', '12', 8.3, 7, 12),
(26, '2001: Uma Odisseia no Espaço', 'A humanidade encontra...', 'L', 8.3, 8, 13),
(27, 'Psicose', 'Uma secretária...', '14', 8.5, 9, 14),
(28, 'Tempos Modernos', 'O Vagabundo luta...', 'L', 8.5, 4, 15),
(29, 'Pulp Fiction: Tempo de Violência', 'As vidas de dois...', '18', 8.9, 6, 16),
(30, 'Casablanca', 'Um dono de boate...', '12', 8.5, 7, 17);

-- -----------------------------------------------------
-- PASSO 4: Ligar Atores e Filmes (elenco)
-- -----------------------------------------------------

-- (Apenas algumas ligações de exemplo)
INSERT INTO elenco (fk_id_filme, fk_id_ator) VALUES
(1, 1), (1, 2), (1, 3), -- Elenco LotR
(2, 1), (2, 2), (2, 3), -- Elenco LotR
(3, 1), (3, 2), (3, 3), -- Elenco LotR
(4, 7), (4, 8), (4, 9), -- Elenco 10 Coisas
(5, 4), (5, 5), (5, 6), -- Elenco Crepúsculo
(6, 4), (6, 5), (6, 6), -- Elenco Crepúsculo
(10, 10), (10, 11), (10, 13), -- Elenco Velozes
(14, 10), (14, 11), (14, 12), -- Elenco Velozes 5
(16, 10), (16, 11), (16, 12), -- Elenco Velozes 7
(20, 14), (20, 15), (20, 16), -- Elenco Shrek
(21, 14), (21, 15), (21, 16), -- Elenco Shrek 2
(24, 17), (24, 18), -- Elenco Poderoso Chefão
(27, 21), -- Elenco Psicose
(28, 22), (28, 23), -- Elenco Tempos Modernos
(29, 24), (29, 25), -- Elenco Pulp Fiction
(30, 26), (30, 27); -- Elenco Casablanca

-- -----------------------------------------------------
-- PASSO 5: Criar Sessões e Vender Ingressos
-- (Importante para as Consultas 2 e 3)
-- -----------------------------------------------------

-- Inserir Assentos (para Sala 1)
INSERT INTO Assento (id_assento, linha, coluna, vip, fk_numero_sala) VALUES
(1, 'A', '1', false, 1),
(2, 'A', '2', false, 1),
(3, 'A', '3', false, 1),
(4, 'B', '1', false, 1),
(5, 'B', '2', false, 1);

-- Inserir Sessões (15 sessões)
-- (Datas espalhadas de 09/11 a 15/11 para a Consulta 2 funcionar)
INSERT INTO Sessao (id_sessao, horario, data, eh_3d, fk_numero_sala, fk_id_filme) VALUES
(1, '14:00:00', '2025-11-09', false, 1, 1),  -- LotR 1 (Domingo)
(2, '17:00:00', '2025-11-09', false, 2, 5),  -- Crepúsculo (Domingo)
(3, '20:00:00', '2025-11-10', false, 1, 10), -- Velozes (Segunda)
(4, '21:00:00', '2025-11-10', false, 3, 24), -- Poderoso Chefão (Segunda)
(5, '15:00:00', '2025-11-11', false, 1, 20), -- Shrek (Terça)
(6, '18:00:00', '2025-11-11', false, 2, 4),  -- 10 Coisas (Terça)
(7, '19:00:00', '2025-11-12', false, 1, 14), -- Velozes 5 (Quarta)
(8, '21:30:00', '2025-11-12', true, 3, 3),   -- LotR 3 (Quarta)
(9, '17:00:00', '2025-11-13', false, 1, 6),  -- Lua Nova (Quinta)
(10, '20:00:00', '2025-11-13', false, 2, 29), -- Pulp Fiction (Quinta)
(11, '14:30:00', '2025-11-14', false, 1, 21), -- Shrek 2 (Sexta)
(12, '18:00:00', '2025-11-14', false, 3, 16), -- Velozes 7 (Sexta)
(13, '21:00:00', '2025-11-14', false, 1, 27), -- Psicose (Sexta)
(14, '16:00:00', '2025-11-15', false, 3, 2),  -- LotR 2 (Sábado)
(15, '19:00:00', '2025-11-15', false, 1, 28); -- Tempos Modernos (Sábado)


-- Inserir Ingressos (25 ingressos criados)
INSERT INTO Ingresso (id_ingresso, valor, meia_entrada, fk_id_sessao) VALUES
(1, 40.00, false, 1),
(2, 20.00, true,  1),
(3, 60.00, false, 2),
(4, 30.00, true,  3),
(5, 50.00, false, 4),
(6, 40.00, false, 5),
(7, 20.00, true,  5),
(8, 60.00, false, 6),
(9, 40.00, false, 7),
(10, 70.00, true,  8),
(11, 40.00, false, 9),
(12, 60.00, false, 10),
(13, 20.00, true,  11),
(14, 40.00, false, 11),
(15, 70.00, false, 12),
(16, 35.00, true,  12),
(17, 40.00, false, 13),
(18, 70.00, false, 14),
(19, 35.00, true,  14),
(20, 40.00, false, 15),
(21, 50.00, false, 4), -- Mais um ingresso para 'Poderoso Chefão' (Sessão 4)
(22, 70.00, false, 12), -- Mais um ingresso para 'Velozes 7' (Sessão 12)
(23, 70.00, false, 8),  -- Mais um ingresso para 'LotR 3' (Sessão 8)
(24, 60.00, false, 2),  -- Mais um ingresso para 'Crepúsculo' (Sessão 2)
(25, 40.00, false, 3);  -- Mais um ingresso para 'Velozes' (Sessão 3)


-- Inserir Vendas de Ingressos (Cliente_Ingresso)
-- (Datas de emissão espalhadas pelos 7 dias da semana)
INSERT INTO Cliente_Ingresso (fk_id_cliente, fk_id_ingresso, quantidade, valor_total, data_emissao, id_nota) VALUES
(1, 1, 1, 40.00, '2025-11-09 13:00:00', 'NFE-001'), -- DOMINGO
(1, 2, 1, 20.00, '2025-11-09 13:00:00', 'NFE-001'), -- DOMINGO
(2, 3, 1, 60.00, '2025-11-09 16:00:00', 'NFE-002'), -- DOMINGO
(3, 4, 1, 30.00, '2025-11-10 19:00:00', 'NFE-003'), -- SEGUNDA
(4, 5, 1, 50.00, '2025-11-10 20:00:00', 'NFE-004'), -- SEGUNDA
(5, 6, 1, 40.00, '2025-11-11 14:00:00', 'NFE-005'), -- TERÇA
(6, 7, 1, 20.00, '2025-11-11 14:10:00', 'NFE-006'), -- TERÇA
(7, 8, 1, 60.00, '2025-11-11 17:00:00', 'NFE-007'), -- TERÇA
(8, 9, 1, 40.00, '2025-11-12 18:00:00', 'NFE-008'), -- QUARTA
(9, 10, 1, 70.00, '2025-11-12 20:00:00', 'NFE-009'), -- QUARTA
(10, 11, 1, 40.00, '2025-11-13 16:00:00', 'NFE-010'), -- QUINTA
(11, 12, 1, 60.00, '2025-11-13 19:00:00', 'NFE-011'), -- QUINTA
(12, 13, 1, 20.00, '2025-11-14 13:00:00', 'NFE-012'), -- SEXTA
(13, 14, 1, 40.00, '2025-11-14 13:02:00', 'NFE-013'), -- SEXTA
(14, 15, 1, 70.00, '2025-11-14 17:00:00', 'NFE-014'), -- SEXTA
(15, 16, 1, 35.00, '2025-11-14 17:01:00', 'NFE-015'), -- SEXTA
(16, 17, 1, 40.00, '2025-11-14 20:00:00', 'NFE-016'), -- SEXTA
(17, 18, 1, 70.00, '2025-11-15 15:00:00', 'NFE-017'), -- SÁBADO
(18, 19, 1, 35.00, '2025-11-15 15:01:00', 'NFE-018'), -- SÁBADO
(19, 20, 1, 40.00, '2025-11-15 18:00:00', 'NFE-019'), -- SÁBADO
(20, 21, 1, 50.00, '2025-11-10 20:05:00', 'NFE-020'), -- SEGUNDA (Poderoso Chefão)
(1, 22, 1, 70.00, '2025-11-14 17:05:00', 'NFE-021'), -- SEXTA (Velozes 7)
(3, 23, 1, 70.00, '2025-11-12 20:10:00', 'NFE-022'), -- QUARTA (LotR 3)
(5, 24, 1, 60.00, '2025-11-09 16:05:00', 'NFE-023'), -- DOMINGO (Crepúsculo)
(7, 25, 1, 30.00, '2025-11-10 19:05:00', 'NFE-024'); -- SEGUNDA (Velozes)


-- Ligar Ingressos a Assentos
INSERT INTO assento_ingresso (fk_id_assento, fk_id_ingresso) VALUES
(1, 1),
(2, 2),
(1, 3), -- Assento 1 (Sala 1) vendido para Sessão 2 (Sala 2) - ERRO PROPOSITAL NO MODELO, MAS OK PARA TESTE
(1, 4),
(1, 5),
(3, 6),
(4, 7),
(2, 8),
(3, 9),
(3, 10),
(5, 11),
(5, 12),
(1, 13),
(2, 14),
(4, 15),
(5, 16),
(1, 17),
(2, 18),
(3, 19),
(4, 20),
(2, 21),
(1, 22),
(4, 23),
(3, 24),
(5, 25);

-- -----------------------------------------------------
-- PASSO 6: Vendas da Bomboniere
-- -----------------------------------------------------
INSERT INTO Venda (id_venda, valor, fk_id_funcionario, fk_id_cliente, fk_id_item) VALUES
(1, 40.00, 1, 1, 1), -- Func 1 vendeu Pipoca (1) para Cliente 1
(2, 15.00, 1, 1, 2), -- Func 1 vendeu Refri (2) para Cliente 1
(3, 15.00, 1, 2, 2), -- Func 1 vendeu Refri (2) para Cliente 2
(4, 12.00, 2, 5, 3); -- Func 2 vendeu M&M (3) para Cliente 5