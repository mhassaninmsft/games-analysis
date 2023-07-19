# from dataclasses import dataclass
from sqlalchemy.orm import sessionmaker
import csv
from sqlalchemy.orm import registry
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import create_engine
import os

DB_HOST = "localhost"
DB_NAME = "gamesdb"
DB_USER = "gamesuser"
DB_PASS = os.getenv("PGPASSWORD")

# @dataclass
# class Game:
#     url: str
#     types: str
#     name: str
#     desc_snippet: str
#     recent_reviews: str
#     all_reviews: str
#     release_date: str
#     developer: str
#     publisher: str
#     popular_tags: str
#     game_details: str
#     languages: str
#     achievements: str
#     genre: str
#     game_description: str
#     mature_content: str
#     minimum_requirements: str
#     recommended_requirements: str
#     original_price: str


# reg = registry()
reg = registry()
# replace with your database URL
engine = create_engine(
    f'postgresql://{DB_USER}:{DB_PASS}@localhost:5432/{DB_NAME}')
Session = sessionmaker(engine)


@reg.mapped_as_dataclass(unsafe_hash=True)
class Game:
    """Game class will be converted to a dataclass"""

    __tablename__ = "game"

    url: Mapped[str] = mapped_column(init=False, primary_key=True)
    types: Mapped[str]
    name: Mapped[str]
    desc_snippet: Mapped[str]
    recent_reviews: Mapped[str]
    all_reviews: Mapped[str]
    release_date: Mapped[str]
    developer: Mapped[str]
    publisher: Mapped[str]
    popular_tags: Mapped[str]
    game_details: Mapped[str]
    languages: Mapped[str]
    achievements: Mapped[str]
    genre: Mapped[str]
    game_description: Mapped[str]
    mature_content: Mapped[str]
    minimum_requirements: Mapped[str]
    recommended_requirements: Mapped[str]
    original_price: Mapped[str]

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


def get_games() -> list[Game]:
    """ This function will read the list of games from the CSV file and return a list of Game objects"""
    games = []
    with open('./data/steam_games.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            game = Game(
                url=row['url'],
                types=row['types'],
                name=row['name'],
                desc_snippet=row['desc_snippet'],
                recent_reviews=row['recent_reviews'],
                all_reviews=row['all_reviews'],
                release_date=row['release_date'],
                developer=row['developer'],
                publisher=row['publisher'],
                popular_tags=row['popular_tags'],
                game_details=row['game_details'],
                languages=row['languages'],
                achievements=row['achievements'],
                genre=row['genre'],
                game_description=row['game_description'],
                mature_content=row['mature_content'],
                minimum_requirements=row['minimum_requirements'],
                recommended_requirements=row['recommended_requirements'],
                original_price=row['original_price']
            )
            # print(game)
            games.append(game)
    return games


def save_games(games: list[Game]):
    session = Session()
    # games = get_games()
    for game in games:
        session.add(game)
    session.commit()

    # for game in games:
    #     try:
    #         session.add(game)
    #         session.commit()
    #     except Exception as e:
    #         session.rollback()
    #         print("Error")
    #         print(e)
    #         print("Game: ")
    #         print(game)
