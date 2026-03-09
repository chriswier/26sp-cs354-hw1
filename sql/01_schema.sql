-- ============================================================
-- hw01-starting-with-sql  |  01_schema.sql
-- Database: manga
-- ============================================================

DROP TABLE IF EXISTS manga;

CREATE TABLE manga (
    id             SERIAL          PRIMARY KEY,
    title          VARCHAR(255)    NOT NULL,
    author         VARCHAR(255)    NOT NULL,
    genre          VARCHAR(100)    NOT NULL,
    status         VARCHAR(50)     NOT NULL,   -- 'Ongoing' | 'Completed'
    avg_rating     NUMERIC(3, 1),              -- NULL allowed (unrated)
    volumes        INTEGER         NOT NULL,
    year_published INTEGER         NOT NULL
);
