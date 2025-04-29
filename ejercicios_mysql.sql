CREATE TABLE Usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100),
    fecha_de_registro DATE
);

INSERT INTO Usuarios (nombre, email, fecha_de_registro) VALUES
('Armando Aquino', 'armando@gmail.com', '2025-04-28'),
('Valentina Muñoz', 'valetina@hotmail.com', '2025-04-01'),
('Agustin Dominguez', 'agustin@outlook.com', '2025-03-15');