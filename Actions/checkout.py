
import datetime
from Actions.actions import ActionsEnum, ChatBotAction
from sqlalchemy.orm import Session
from models import DbConnection, Game, Purchase, ShoppingCart
from globals import user_id


class CheckoutAction(ChatBotAction):
    def __init__(self):
        self.db_connection = DbConnection()
        pass

    def execute(self) -> ActionsEnum:
        """Main entrypoint in the Checkout workflow."""
        session = self.db_connection.get_session()
        buy_games_from_user_cart(session)
        return ActionsEnum.End


def buy_games_from_user_cart(session: Session) -> list[int]:
    """Get the user cart."""
    games_in_cart = session.query(ShoppingCart).filter(
        ShoppingCart.customer_id == user_id).all()
    game_ids = [game.game_id for game in games_in_cart]
    # Add Games to the list of purchased games
    for game_id in game_ids:
        purchase = Purchase(customer_id=user_id, game_id=game_id,
                            created_at=datetime.datetime.now())
        session.add(purchase)
    # Delete the games from the cart
    for game in games_in_cart:
        session.delete(game)
    session.commit()
