CREATE TABLE customer (
  id SERIAL PRIMARY KEY,
  username TEXT,
  email TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE purchase (
  id SERIAL PRIMARY KEY,
  customer_id INTEGER REFERENCES customer(id),
  game_id INTEGER REFERENCES game(id),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE complaint (
  id SERIAL PRIMARY KEY,
  complaint TEXT,
  customer_id INTEGER REFERENCES customer(id),
  purchase_id INTEGER REFERENCES purchase(id),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
-- shopping cart table 
CREATE TABLE shopping_cart (
  id SERIAL PRIMARY KEY,
  customer_id INTEGER REFERENCES customer(id),
  game_id INTEGER REFERENCES game(id),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);