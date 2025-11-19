-- init_db.sql
-- Script to create minimal schema and a sample admin user for development

CREATE DATABASE IF NOT EXISTS contabilidad_db;
USE contabilidad_db;

-- Table: usuarios
CREATE TABLE IF NOT EXISTS usuarios (
  id_usuario INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(150) NOT NULL,
  correo VARCHAR(200) NOT NULL UNIQUE,
  rol VARCHAR(50) NOT NULL DEFAULT 'cliente',
  contrasena_hash VARCHAR(255) NOT NULL,
  saldo DECIMAL(15,2) NOT NULL DEFAULT 0.00,
  creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table: bolsillos
CREATE TABLE IF NOT EXISTS bolsillos (
  id_bolsillo INT AUTO_INCREMENT PRIMARY KEY,
  usuario_id INT NOT NULL,
  nombre VARCHAR(150) NOT NULL,
  fecha_creacion DATE DEFAULT (CURRENT_DATE()),
  monto DECIMAL(15,2) NOT NULL DEFAULT 0.00,
  FOREIGN KEY (usuario_id) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table: pagos_automaticos
CREATE TABLE IF NOT EXISTS pagos_automaticos (
  id_pago INT AUTO_INCREMENT PRIMARY KEY,
  usuario_id INT NOT NULL,
  nombre VARCHAR(150) NOT NULL,
  monto DECIMAL(15,2) NOT NULL,
  fecha DATE NOT NULL,
  creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (usuario_id) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Sample admin user (email: admin@example.com, password stored in contrasena_hash)
-- In this simple dev setup the contrasena_hash is stored as plain text; replace by a real hash in production.
INSERT INTO usuarios (nombre, correo, rol, contrasena_hash, saldo)
VALUES ('Administrador', 'admin@example.com', 'admin', 'admin123', 0.00)
ON DUPLICATE KEY UPDATE nombre=VALUES(nombre), rol=VALUES(rol);

-- Optional: sample normal user
INSERT INTO usuarios (nombre, correo, rol, contrasena_hash, saldo)
VALUES ('Usuario Ejemplo', 'usuario@example.com', 'cliente', 'user1234', 50000.00)
ON DUPLICATE KEY UPDATE nombre=VALUES(nombre);

SELECT 'init_db completed' as info;
