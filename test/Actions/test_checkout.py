# Tests the checkout action

from Actions.actions import ActionsEnum, ChatBotAction, GetAction
from Actions.checkout import CheckoutAction
from Actions.search_game import GameSearchAction


# def test_checkout():
#     """Tests the checkout action."""
#     current_action: ChatBotAction = CheckoutAction()
#     while True:
#         current_action = current_action.execute()
#         if current_action == ActionsEnum.End:
#             print("Ending Conversation")
#             break
#         else:
#             print("Domryjinh new returned")
#             current_action = GetAction(current_action)
