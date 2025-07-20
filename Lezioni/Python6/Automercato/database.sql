-- Tabella filiali
CREATE TABLE filiali (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL, -- Nome della filiale
    indirizzo VARCHAR(255) NOT NULL -- Indirizzo completo
);

-- Tabella motociclette
CREATE TABLE motociclette (
    id SERIAL PRIMARY KEY,
    marca VARCHAR(100) NOT NULL,
    modello VARCHAR(100) NOT NULL,
    prezzo DECIMAL NOT NULL,
    disponibilita BOOLEAN NOT NULL,
    filiale_id INT, -- Riferimento alla filiale
    CONSTRAINT fk_motociclette_filiali FOREIGN KEY (filiale_id) REFERENCES filiali (id) ON DELETE SET NULL
);

-- Tabella automobili
CREATE TABLE automobili (
    id SERIAL PRIMARY KEY,
    marca VARCHAR(100) NOT NULL,
    modello VARCHAR(100) NOT NULL,
    prezzo DECIMAL NOT NULL,
    disponibilita BOOLEAN NOT NULL,
    filiale_id INT, -- Riferimento alla filiale
    CONSTRAINT fk_automobili_filiali FOREIGN KEY (filiale_id) REFERENCES filiali (id) ON DELETE SET NULL
);

-- Tabella accessori
CREATE TABLE accessori (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    categoria VARCHAR(100) NOT NULL,
    prezzo DECIMAL(10, 2) NOT NULL,
    disponibilita BOOLEAN NOT NULL,
    filiale_id INT, -- Riferimento alla filiale
    CONSTRAINT fk_accessori_filiali FOREIGN KEY (filiale_id) REFERENCES filiali (id) ON DELETE SET NULL
);

-- Tabella operator
CREATE TABLE operator (
    id SERIAL PRIMARY KEY,
    password VARCHAR(255) NOT NULL,
    admin BOOLEAN NOT NULL
);

-- Tabella vendite
CREATE TABLE vendite (
    id SERIAL PRIMARY KEY,
    filiale_id INT NOT NULL,
    oggetto_id INT NOT NULL,
    tipo_oggetto VARCHAR(50) NOT NULL,
    data_vendita DATE NOT NULL,
    CONSTRAINT fk_vendite_filiali FOREIGN KEY (filiale_id) REFERENCES filiali (id) ON DELETE CASCADE
);

INSERT INTO filiali (nome, indirizzo) VALUES
('Filiale Roma', 'Via Roma, 1'),
('Filiale Milano', 'Corso Milano, 20'),
('Filiale Napoli', 'Piazza Napoli, 3'),
('Filiale Torino', 'Via Torino, 15');
INSERT INTO motociclette (marca, modello, prezzo, disponibilita, filiale_id) VALUES
('Yamaha', 'MT-07', 7500.00, TRUE, 1),
('Kawasaki', 'Ninja 400', 6500.00, TRUE, 2),
('Honda', 'CB500F', 7200.00, TRUE, 3),
('Ducati', 'Monster', 10500.00, TRUE, 4),
('BMW', 'F 900 R', 11200.00, TRUE, 1),
('Suzuki', 'V-Strom 650', 8200.00, TRUE, 2),
('KTM', 'Duke 390', 6800.00, TRUE, 3),
('Triumph', 'Street Triple', 9500.00, TRUE, 4),
('Harley-Davidson', 'Iron 883', 11500.00, TRUE, 1),
('Aprilia', 'RS 660', 10300.00, TRUE, 2),
('Yamaha', 'R6', 12500.00, TRUE, 3),
('Kawasaki', 'Z650', 7500.00, TRUE, 4),
('Honda', 'Africa Twin', 14200.00, TRUE, 1),
('Ducati', 'Scrambler', 9600.00, TRUE, 2),
('BMW', 'R 1250 GS', 16000.00, TRUE, 3),
('Suzuki', 'GSX-R750', 11700.00, TRUE, 4),
('KTM', 'RC 390', 7000.00, TRUE, 1),
('Triumph', 'Bonneville T100', 11500.00, TRUE, 2),
('Harley-Davidson', 'Street 750', 8000.00, TRUE, 3),
('Aprilia', 'Tuono 660', 11300.00, TRUE, 4);
INSERT INTO automobili (marca, modello, prezzo, disponibilita, filiale_id) VALUES
('Toyota', 'Corolla', 23000.00, TRUE, 1),
('Ford', 'Focus', 21000.00, TRUE, 2),
('Volkswagen', 'Golf', 25000.00, TRUE, 3),
('BMW', 'Serie 3', 40000.00, TRUE, 4),
('Mercedes', 'Classe A', 35000.00, TRUE, 1),
('Fiat', 'Panda', 12000.00, TRUE, 2),
('Peugeot', '208', 20000.00, TRUE, 3),
('Renault', 'Clio', 19000.00, TRUE, 4),
('Audi', 'A3', 37000.00, TRUE, 1),
('Tesla', 'Model 3', 50000.00, TRUE, 2),
('Hyundai', 'Tucson', 29000.00, TRUE, 3),
('Kia', 'Sportage', 28000.00, TRUE, 4),
('Mazda', 'CX-5', 32000.00, TRUE, 1),
('Honda', 'Civic', 24000.00, TRUE, 2),
('Dacia', 'Duster', 18000.00, TRUE, 3),
('Suzuki', 'Vitara', 22000.00, TRUE, 4),
('Opel', 'Corsa', 17000.00, TRUE, 1),
('Nissan', 'Qashqai', 30000.00, TRUE, 2),
('Jeep', 'Renegade', 26000.00, TRUE, 3),
('Volvo', 'XC40', 45000.00, TRUE, 4);
INSERT INTO accessori (nome, categoria, prezzo, disponibilita, filiale_id) VALUES
('Casco Integrale', 'Caschi', 300.00, TRUE, 1),
('Gomme Estive', 'Pneumatici', 600.00, TRUE, 2),
('Portapacchi', 'Bagagli', 150.00, TRUE, 3),
('Navigatore GPS', 'Elettronica', 250.00, TRUE, 4),
('Parabrezza', 'Protezione', 200.00, TRUE, 1),
('Lucchetto', 'Sicurezza', 50.00, TRUE, 2),
('Batteria Auto', 'Elettronica', 120.00, TRUE, 3),
('Telo Coprimoto', 'Coperture', 70.00, TRUE, 4),
('Catene da Neve', 'Sicurezza', 100.00, TRUE, 1),
('Kit Riparazione', 'Manutenzione', 80.00, TRUE, 2),
('Casco Jet', 'Caschi', 200.00, TRUE, 3),
('Gomme Invernali', 'Pneumatici', 650.00, TRUE, 4),
('Kit Attrezzi', 'Manutenzione', 90.00, TRUE, 1),
('Baule Posteriore', 'Bagagli', 400.00, TRUE, 2),
('Fari LED', 'Elettronica', 180.00, TRUE, 3),
('Guanti Protettivi', 'Protezione', 100.00, TRUE, 4),
('Paraschiena', 'Protezione', 250.00, TRUE, 1),
('Cavalletto Centrale', 'Manutenzione', 140.00, TRUE, 2),
('Giacca Protettiva', 'Abbigliamento', 350.00, TRUE, 3),
('Copertura Auto', 'Coperture', 100.00, TRUE, 4);
INSERT INTO operator (password, admin) VALUES
('Zagarolo', TRUE),
('password2', FALSE),
('password3', FALSE),
('password4', TRUE),
('password5', FALSE),
('password6', TRUE),
('password7', FALSE),
('password8', FALSE),
('password9', TRUE),
('password10', FALSE),
('password11', FALSE),
('password12', TRUE),
('password13', TRUE),
('password14', FALSE),
('password15', FALSE),
('password16', TRUE),
('password17', FALSE),
('password18', FALSE),
('password19', TRUE),
('password20', FALSE);
-- Vendite di esempio con oggetto_id tra 1 e 8
INSERT INTO vendite (filiale_id, oggetto_id, tipo_oggetto, data_vendita) VALUES
(1, 1, 'automobile', '2024-11-01'), -- Automobile ID 1 venduta dalla Filiale Roma
(2, 2, 'motocicletta', '2024-11-02'), -- Motocicletta ID 2 venduta dalla Filiale Milano
(3, 3, 'accessorio', '2024-11-03'),  -- Accessorio ID 3 venduto dalla Filiale Napoli
(4, 4, 'automobile', '2024-11-04'), -- Automobile ID 4 venduta dalla Filiale Torino
(1, 5, 'motocicletta', '2024-11-05'), -- Motocicletta ID 5 venduta dalla Filiale Roma
(2, 6, 'accessorio', '2024-11-06'), -- Accessorio ID 6 venduto dalla Filiale Milano
(3, 7, 'automobile', '2024-11-07'), -- Automobile ID 7 venduta dalla Filiale Napoli
(4, 8, 'motocicletta', '2024-11-08'), -- Motocicletta ID 8 venduta dalla Filiale Torino
(1, 2, 'automobile', '2024-11-09'), -- Automobile ID 2 venduta dalla Filiale Roma
(2, 3, 'motocicletta', '2024-11-10'), -- Motocicletta ID 3 venduta dalla Filiale Milano
(3, 4, 'accessorio', '2024-11-11'),  -- Accessorio ID 4 venduto dalla Filiale Napoli
(4, 5, 'automobile', '2024-11-12'), -- Automobile ID 5 venduta dalla Filiale Torino
(1, 6, 'motocicletta', '2024-11-13'), -- Motocicletta ID 6 venduta dalla Filiale Roma
(2, 7, 'accessorio', '2024-11-14'), -- Accessorio ID 7 venduto dalla Filiale Milano
(3, 8, 'automobile', '2024-11-15'), -- Automobile ID 8 venduta dalla Filiale Napoli
(4, 1, 'motocicletta', '2024-11-16'), -- Motocicletta ID 1 venduta dalla Filiale Torino
(1, 3, 'automobile', '2024-11-17'), -- Automobile ID 3 venduta dalla Filiale Roma
(2, 4, 'motocicletta', '2024-11-18'), -- Motocicletta ID 4 venduta dalla Filiale Milano
(3, 5, 'accessorio', '2024-11-19'),  -- Accessorio ID 5 venduto dalla Filiale Napoli
(4, 6, 'automobile', '2024-11-20'); -- Automobile ID 6 venduta dalla Filiale Torino
