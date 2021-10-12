DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS characters;


CREATE TABLE users(
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(20) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE characters(
    character_id SERIAL PRIMARY KEY,
    creator_id INT NOT NULL FOREIGN KEY REFERENCES users(user_id)
    char_name VARCHAR(30) NOT NULL
);