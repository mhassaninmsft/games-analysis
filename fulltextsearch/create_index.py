
import os
from dataclasses import dataclass
import uuid
from dataclasses_json import dataclass_json
from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    ComplexField,
    CorsOptions,
    SearchIndex,
    ScoringProfile,
    SearchFieldDataType,
    SimpleField,
    SearchableField
)

from models import Game

endpoint = os.environ["SEARCH_ENDPOINT"]
key = os.environ["SEARCH_API_KEY"]


@dataclass
# @dataclass_json
class GameSearchObject:
    gameId: str
    gameUrl: str
    gameName: str
    description: str
    reviews: str

    # Make static method

    @staticmethod
    def from_game(game: Game) -> "GameSearchObject":
        # generate uuids as ids
        id = uuid.uuid4()
        return GameSearchObject(
            gameId=str(id),
            gameUrl=game.url,
            gameName=game.name,
            description=game.game_description,
            reviews=game.all_reviews
        )


def bootstrap_index():
    # Create a service client
    client = SearchIndexClient(endpoint, AzureKeyCredential(key))

    # Create the index
    name = "games"
    fields = [
        SimpleField(name="gameId", type=SearchFieldDataType.String, key=True),
        SearchableField(name="gameUrl", type=SearchFieldDataType.String),
        SearchableField(name="gameName", type=SearchFieldDataType.String),
        SearchableField(name="description", type=SearchFieldDataType.String),
        SearchableField(name="reviews", type=SearchFieldDataType.String),
        # ComplexField(name="address", fields=[
        #     SimpleField(name="streetAddress", type=SearchFieldDataType.String),
        #     SimpleField(name="city", type=SearchFieldDataType.String),
        # ])
    ]
    cors_options = CorsOptions(allowed_origins=["*"], max_age_in_seconds=60)
    scoring_profiles = []

    index = SearchIndex(
        name=name,
        fields=fields,
        scoring_profiles=scoring_profiles,
        cors_options=cors_options)

    result = client.create_index(index)
    print("Create Indexes succeeded: {}".format(result))
