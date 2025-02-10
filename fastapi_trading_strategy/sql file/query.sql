CREATE TABLE stock_data (
    id SERIAL PRIMARY KEY,
    datetime TIMESTAMP NOT NULL,
    open DECIMAL(10,2) NOT NULL,
    high DECIMAL(10,2) NOT NULL,
    low DECIMAL(10,2) NOT NULL,
    close DECIMAL(10,2) NOT NULL,
    volume INTEGER NOT NULL
);
