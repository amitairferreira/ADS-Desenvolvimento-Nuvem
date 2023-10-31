CREATE DATABASE professionals;
USE professionals;


CREATE TABLE professionals_data (
  Name VARCHAR(50),
  Contact VARCHAR(50),
  Specialization (100)
);


INSERT INTO professionals_data
  (Name, Contact, Specialization)
VALUES
  ('Alice Cristina Freitas', 'alicepsi@email.com', 'Depressão/Ansiedade'),
  ('Maria Helena Benevides', 'mariapsicol@email.com', 'TEA/TDAH'),
  ('João Pedro de Sá', 'joaopsi@email.com', 'Depressão/Ansiedade');