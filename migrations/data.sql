INSERT INTO customer (id, username, email, created_at) VALUES
(1, 'JohnDoe', 'johndoe@example.com', '2023-07-01 12:30:00'),
(2, 'JaneDoe', 'janedoe@example.com', '2023-07-02 13:45:00'),
(3, 'AlexSmith', 'alexsmith@example.com', '2023-07-10 15:00:00');

INSERT INTO purchase (id, customer_id, game_id, created_at) VALUES
(1, 1, 1, '2023-07-02 14:00:00'),
(2, 1, 2, '2023-07-02 14:15:00'),
(3, 2, 1, '2023-07-03 10:30:00');

INSERT INTO complaint (id, complaint, customer_id, game_id, created_at) VALUES
(1, 'Game crashes after launch', 1, 1, '2023-07-03 14:30:00'),
(2, 'Game does not meet the system requirements mentioned', 2, 2, '2023-07-04 09:00:00'),
(3, 'Achievements not unlocking properly', 1, 2, '2023-07-05 16:00:00');

INSERT INTO shopping_cart (id, customer_id, game_id, created_at) VALUES
(1, 1, 3, '2023-07-02 14:30:00'),
(2, 2, 4, '2023-07-03 11:00:00'),
(3, 1, 5, '2023-07-06 17:00:00');
