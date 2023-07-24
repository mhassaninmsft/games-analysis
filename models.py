# from dataclasses import dataclass
import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

import csv
from sqlalchemy.orm import registry
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey, create_engine
from dataclasses_json import dataclass_json
import os

DB_HOST = "database"  # "localhost"
DB_NAME = "gamesdb"
DB_USER = "gamesuser"
DB_PASS = os.getenv("PGPASSWORD")

# reg = registry()
reg = registry()
reg.configure(True)
# replace with your database URL
engine = create_engine(
    f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}')
Session = sessionmaker(engine)


class DbConnection:
    def __init__(self):
        self.engine = create_engine(
            f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}')
        self.session = Session

    def get_session(self):
        return self.session()


@reg.mapped_as_dataclass(unsafe_hash=True)
@dataclass_json
class Game:
    """Game class will be converted to a dataclass"""
    __tablename__ = "game"
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    url: Mapped[str]
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


@reg.mapped_as_dataclass(unsafe_hash=True)
@dataclass_json
class Customer:
    __tablename__ = "customer"
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    username: Mapped[str]
    email: Mapped[str]
    created_at: Mapped[datetime.datetime]

    # purchases = relationship("Purchase", back_populates="purchase")
    # complaints = relationship("Complaint", back_populates="customer")
    # shopping_carts = relationship("ShoppingCart", back_populates="customer")

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


@reg.mapped_as_dataclass(unsafe_hash=True)
@dataclass_json
class Purchase:
    __tablename__ = "purchase"
    # id is populated by the database
    id: Mapped[int] = mapped_column(
        init=False, primary_key=True, autoincrement=True)
    # id: Mapped[int] = mapped_column(init=False, primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey('customer.id'))
    # customer: relationship('Customer')
    game_id: Mapped[int] = mapped_column(ForeignKey('game.id'))
    # game: relationship('Game')
    created_at: Mapped[datetime.datetime]

    customer = relationship("Customer", backref="purchases")

    # customer = relationship("Customer", back_populates="purchases")

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


@reg.mapped_as_dataclass(unsafe_hash=True)
@dataclass_json
class Complaint:
    __tablename__ = "complaint"
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    complaint: Mapped[str]
    customer_id: Mapped[int] = mapped_column(ForeignKey('customer.id'))
    # customer: relationship('Customer')
    purchase_id: Mapped[int] = mapped_column(ForeignKey('purchase.id'))
    # game: relationship('Game')
    created_at: Mapped[datetime.datetime]

    # user = relationship("User", back_populates="complaints")
    # game = relationship("Game", back_populates="complaints")

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


@reg.mapped_as_dataclass(unsafe_hash=True)
@dataclass_json
class ShoppingCart:
    __tablename__ = "shopping_cart"
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey('customer.id'))
    # customer: relationship('Customer')
    game_id: Mapped[int] = mapped_column(ForeignKey('game.id'))
    # game: relationship('Game')
    created_at: Mapped[datetime.datetime] = mapped_column(init=False)

    # customer = relationship("Customer", back_populates="shopping_carts")
    # game = relationship("Game", back_populates="shopping_carts")

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


def get_games() -> list[Game]:
    """ This function will read the list of games from the CSV file and return
      a list of Game objects"""
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


def get_games_from_database() -> list[Game]:
    session = Session()
    games = session.query(Game).all()
    return games


def get_games_from_database_by_url(url: str) -> list[Game]:
    session = Session()
    games = session.query(Game).filter(Game.url == url).all()
    return games


def get_complaints_from_database() -> list[Purchase]:
    session = Session()
    complaints = session.query(Purchase).all()
    comp1 = complaints[0]
    print(comp1.customer)
    return complaints
