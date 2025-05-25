CREATE DATABASE adega;
USE adega;

CREATE TABLE tbl_fabricantes (
    id_fabricante INT AUTO_INCREMENT PRIMARY KEY,
    nome_fabricante VARCHAR(100),
    pais_origem VARCHAR(100)
);

CREATE TABLE tbl_vinhos (
    id_vinho INT AUTO_INCREMENT PRIMARY KEY,
    nome_vinho VARCHAR(100),
    tipo_vinho VARCHAR(100),
    safra DATE,
    quantidade FLOAT,
    valor_vinho DECIMAL(10, 2),
    fgk_fabricante INT,
    venda BOOLEAN DEFAULT false,
    FOREIGN KEY (fgk_fabricante) REFERENCES tbl_fabricantes(id_fabricante)
);

CREATE TABLE tbl_pedidos (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    data_pedido DATE NOT NULL,
    nome_cliente VARCHAR(100) NOT NULL,
    fgk_vinho INT,
    FOREIGN KEY (fgk_vinho) REFERENCES tbl_vinhos(id_vinho)
);

INSERT INTO tbl_fabricantes (nome_fabricante, pais_origem) VALUES
('Vinícola Aurora', 'Brasil'),
('Casa Valduga', 'Brasil'),
('Miolo Wine Group', 'Brasil'),
('Salton', 'Brasil'),
('Dom Bosco', 'Brasil'),
('Concha y Toro', 'Chile'),
('Trapiche', 'Argentina'),
('Gallo Family', 'EUA'),
('Baron Philippe de Rothschild', 'França'),
('Penfolds', 'Austrália'),
('Quatre Amis', 'Brasil');

INSERT INTO tbl_vinhos (nome_vinho, tipo_vinho, safra, quantidade, valor_vinho, fgk_fabricante) VALUES
('Aurora Reserva', 'Tinto Seco', '2020-01-01', 750, 2500.00, 1),
('Valduga Chardonnay', 'Branco Seco', '2021-01-01', 750, 3200.00, 2),
('Miolo Merlot', 'Tinto Seco', '2019-01-01', 750, 2800.00, 3),
('Valduga Espumante', 'Espumante Brut', '2022-01-01', 1500, 3500.00, 2),
('Salton', 'Tinto Seco', '2018-01-01', 750, 2300.00, 4),
('Dom Bosco', 'Tinto Suave', '2021-01-01', 750, 2100.00, 5),
('Aurora Moscato', 'Branco Suave', '2022-01-01', 375, 2600.00, 1),
('Miolo Seleção', 'Rosé Seco', '2023-01-01', 750, 2900.00, 3),
('Casa Valduga Terroir', 'Tinto Seco', '2020-01-01', 1500, 4200.00, 2),
('Concha y Toro Reservado', 'Tinto Seco', '2021-01-01', 3000, 3100.00, 6),
('Trapiche Oak Cask', 'Tinto Seco', '2020-01-01', 750, 2700.00, 7),
('Gallo Cabernet Sauvignon', 'Tinto Seco', '2021-01-01', 750, 2500.00, 8),
('Rothschild Bordeaux', 'Tinto Seco', '2019-01-01', 750, 4700.00, 9),
('Penfolds Bin 28', 'Tinto Seco', '2020-01-01', 750, 5200.00, 10),
('Order by Cabernet', 'Reserva', '2018-01-01', 750, 6900.00, 11),
('Python Noir', 'Tinto', '2022-11-25', 750, 7990.00, 11),
('Scrum Merlot', 'Merlot', '2022-11-10', 750, 5774.50, 11),
('Miolo Lote 43', 'Tinto Seco', '2020-01-01', 750, 3800.00, 3),
('Salton Brut Rosé', 'Espumante Brut Rosé', '2022-01-01', 750, 2900.00, 4),
('Dom Bosco Branco Suave', 'Branco Suave', '2021-01-01', 750, 2000.00, 5),
('Aurora Pinot Noir', 'Tinto Seco', '2021-01-01', 750, 3100.00, 1),
('Casa Valduga Identidade', 'Branco Seco', '2023-01-01', 750, 3400.00, 2);


INSERT INTO tbl_pedidos (data_pedido, nome_cliente, fgk_vinho) VALUES
('2024-05-10', 'João Silva', 1),
('2024-05-11', 'Maria Oliveira', 2),
('2024-05-12', 'Carlos Souza', 3),
('2024-05-13', 'Ana Paula', 4),
('2024-05-14', 'Pedro Santos', 5),
('2024-05-15', 'Fernanda Lima', 6),
('2024-05-16', 'Lucas Pereira', 7),
('2024-05-17', 'Juliana Costa', 8),
('2024-05-18', 'Rafael Almeida', 9),
('2024-05-19', 'Camila Rocha', 10);

