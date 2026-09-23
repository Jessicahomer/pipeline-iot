-- View 1: média de temperatura por ambiente
CREATE OR REPLACE VIEW avg_temp_por_ambiente AS
SELECT
    room_id,
    ROUND(AVG(temperature), 2) AS avg_temperature
FROM temperature_readings
GROUP BY room_id
ORDER BY avg_temperature DESC;


-- View 2: quantidade de leituras por dia
CREATE OR REPLACE VIEW leituras_por_dia AS
SELECT
    DATE(noted_date) AS data,
    COUNT(*) AS quantidade_leituras
FROM temperature_readings
GROUP BY DATE(noted_date)
ORDER BY data;


-- View 3: temperaturas máxima e mínima por dia
CREATE OR REPLACE VIEW temp_max_min_por_dia AS
SELECT
    DATE(noted_date) AS data,
    MAX(temperature) AS temp_max,
    MIN(temperature) AS temp_min
FROM temperature_readings
GROUP BY DATE(noted_date)
ORDER BY data;