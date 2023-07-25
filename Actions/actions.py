# Create an actions enum

from abc import ABC, abstractmethod
from enum import Enum


class ActionsEnum(Enum):
    """ Actions Enum """
    ProductSearchOrPurchase = "ProductSearchOrPurchase"
    FaQSearch = "FaQSearch"
    Complaint = "Complaint"
    CheckOut = "CheckOut"
    End = "End"

# Interface for the actions


class ChatBotAction(ABC):

    @abstractmethod
    def execute(self) -> ActionsEnum:
        """ Execute the action."""
        pass


def GetAction(action: ActionsEnum) -> ChatBotAction:
    """ Get the action."""
    pass
    # if action == ActionsEnum.ProductSearch:
    #     return ProductSearchAction()
    # elif action == ActionsEnum.FaQSearch:
    #     return FaQSearchAction()
    # elif action == ActionsEnum.Complaint:
    #     return ComplaintAction()
    # elif action == ActionsEnum.Inquire:
    #     return InquireAction()
    # elif action == ActionsEnum.End:
    #     return EndAction()
    # else:
    #     raise Exception("Invalid action")
