from get_games import Game
import psycopg2
import os
DB_HOST = "localhost"
DB_NAME = "gamesdb"
DB_USER = "gamesuser"
DB_PASS = os.getenv(" PGPASSWORD")

# conn = psycopg2.connect(host=DB_HOST, database=DB_NAME,
#                         user=DB_USER, password=DB_PASS)


# class GamesDatabase:
#     """ Games Database """

#     def __init__(self):
#         conn = psycopg2.connect(host=DB_HOST, database=DB_NAME,
#                                 user=DB_USER, password=DB_PASS)
#         self.conn = conn

#     def insert_game(self, game: Game):
#         """ Insert Game into database """

#         sql = "INSERT INTO games VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#         cursor = self.conn.cursor()
#         cursor.execute(sql, tuple(game))
#         self.conn.commit()

#     def get_game_by_name(self, name):
#         """ Get game by name """

#         sql = "SELECT * FROM games WHERE name = %s"
#         cursor = self.conn.cursor()
#         cursor.execute(sql, (name,))

#         return cursor.fetchone()

#     def get_games_by_developer(self, developer):
#         """ Get games by developer """

#         sql = "SELECT * FROM games WHERE developer = %s"
#         cursor = self.conn.cursor()
#         cursor.execute(sql, (developer,))

#         return cursor.fetchall()


# # Parse CSV and insert games
# with open('games.csv') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         game = Game(**row)
#         insert_game(game)
