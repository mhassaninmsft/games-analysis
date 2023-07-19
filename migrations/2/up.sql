CREATE TABLE user (
  id SERIAL PRIMARY KEY,
  username TEXT,
  email TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE order (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES user(id),
  game_id INTEGER REFERENCES game(id),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE complaint (
  id SERIAL PRIMARY KEY,
  complaint TEXT,
  user_id INTEGER REFERENCES user(id),
  game_id INTEGER REFERENCES game(id),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
-- shopping cart table 
CREATE TABLE shopping_cart (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES user(id),
  game_id INTEGER REFERENCES game(id),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);