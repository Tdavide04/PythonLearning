
CREATE TABLE filiali (
    partita_iva CHAR(11) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    indirizzo_sede VARCHAR(200) NOT NULL,
    civico VARCHAR(10) NOT NULL,
    telefono VARCHAR(15) NOT NULL
);

CREATE TABLE case_in_vendita (
    catastale CHAR(20) PRIMARY KEY,
    indirizzo VARCHAR(200) NOT NULL,
    numero_civico VARCHAR(10) NOT NULL,
    piano INT NOT NULL,
    metri INT NOT NULL CHECK (metri > 0),
    vani INT NOT NULL CHECK (vani > 0),
    prezzo DECIMAL(12, 2) NOT NULL CHECK (prezzo > 0),
    stato VARCHAR(10) NOT NULL CHECK (stato IN ('LIBERO', 'OCCUPATO')),
    filiale_proponente CHAR(11) NOT NULL,
    FOREIGN KEY (filiale_proponente) REFERENCES filiali(partita_iva)
);

CREATE TABLE case_in_affitto (
    catastale CHAR(20) PRIMARY KEY,
    indirizzo VARCHAR(200) NOT NULL,
    civico VARCHAR(10) NOT NULL,
    tipo_affitto VARCHAR(10) NOT NULL CHECK (tipo_affitto IN ('PARZIALE', 'TOTALE')),
    bagno_personale BOOLEAN NOT NULL,
    prezzo_mensile DECIMAL(10, 2) NOT NULL CHECK (prezzo_mensile > 0),
    filiale_proponente CHAR(11) NOT NULL,
    FOREIGN KEY (filiale_proponente) REFERENCES filiali(partita_iva)
);

CREATE TABLE vendite_casa (
    catastale CHAR(20) NOT NULL,
    data_vendita DATE NOT NULL,
    filiale_proponente CHAR(11) NOT NULL,
    filiale_venditrice CHAR(11) NOT NULL,
    prezzo_vendita DECIMAL(12, 2) NOT NULL CHECK (prezzo_vendita > 0),
    PRIMARY KEY (catastale, data_vendita),
    FOREIGN KEY (catastale) REFERENCES case_in_vendita(catastale),
    FOREIGN KEY (filiale_proponente) REFERENCES filiali(partita_iva),
    FOREIGN KEY (filiale_venditrice) REFERENCES filiali(partita_iva)
);

CREATE TABLE affitti_casa (
    catastale CHAR(20) NOT NULL,
    data_affitto DATE NOT NULL,
    filiale_proponente CHAR(11) NOT NULL,
    filiale_venditrice CHAR(11) NOT NULL,
    prezzo_affitto DECIMAL(10, 2) NOT NULL CHECK (prezzo_affitto > 0),
    durata_contratto INT NOT NULL CHECK (durata_contratto > 0),
    PRIMARY KEY (catastale, data_affitto),
    FOREIGN KEY (catastale) REFERENCES case_in_affitto(catastale),
    FOREIGN KEY (filiale_proponente) REFERENCES filiali(partita_iva),
    FOREIGN KEY (filiale_venditrice) REFERENCES filiali(partita_iva)
);

CREATE TABLE operatore (
    id SERIAL PRIMARY KEY,
    password VARCHAR(255) NOT NULL,
    admin BOOLEAN NOT NULL
);

INSERT INTO operatore (password, admin) VALUES
('Zagarolo', TRUE),
('password2', FALSE),
('password3', FALSE),
('password4', TRUE),
('password5', FALSE),
('password6', TRUE)

INSERT INTO filiali (partita_iva, nome, indirizzo_sede, civico, telefono) VALUES
('12345678901', 'Filiale Roma', 'Via Nazionale', '25', '0678912345'),
('23456789012', 'Filiale Milano', 'Corso Buenos Aires', '10', '0287654321'),
('34567890123', 'Filiale Napoli', 'Piazza Garibaldi', '5', '0811234567');

INSERT INTO case_in_vendita (catastale, indirizzo, numero_civico, piano, metri, vani, prezzo, stato, filiale_proponente) VALUES
('A123', 'Via Appia', '50', 2, 80, 3, 200000.00, 'LIBERO', '12345678901'),
('B456', 'Viale Europa', '30', 1, 100, 4, 250000.00, 'OCCUPATO', '12345678901'),
('C789', 'Via Dante', '15', 3, 120, 5, 300000.00, 'LIBERO', '23456789012');

INSERT INTO case_in_affitto (catastale, indirizzo, civico, tipo_affitto, bagno_personale, prezzo_mensile, filiale_proponente) VALUES
('D123', 'Via Roma', '12', 'TOTALE', TRUE, 1200.00, '12345678901'),
('E456', 'Via Milano', '22', 'PARZIALE', FALSE, 700.00, '23456789012'),
('F789', 'Corso Umberto', '8', 'TOTALE', TRUE, 1500.00, '34567890123');

INSERT INTO vendite_casa (catastale, data_vendita, filiale_proponente, filiale_venditrice, prezzo_vendita) VALUES
('A123', '2024-01-15', '12345678901', '23456789012', 195000.00),
('B456', '2024-02-10', '12345678901', '34567890123', 240000.00);

INSERT INTO affitti_casa (catastale, data_affitto, filiale_proponente, filiale_venditrice, prezzo_affitto, durata_contratto) VALUES
('D123', '2024-03-01', '12345678901', '23456789012', 1200.00, 12),
('E456', '2024-04-01', '23456789012', '34567890123', 700.00, 6),
('F789', '2024-05-01', '34567890123', '12345678901', 1500.00, 24);
