import os

import pytest
from openapi_client.api.action_api import ActionApi
from openapi_client.api.info_api import InfoApi
from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration
from openapi_client.models.announce_request import AnnounceRequest
from openapi_client.models.ban_request import BanRequest
from openapi_client.models.kick_request import KickRequest
from openapi_client.models.shutdown_request import ShutdownRequest
from openapi_client.models.unban_request import UnbanRequest


@pytest.fixture
def client():
    configuration = Configuration(
        host=os.environ["HOST"],
        username=os.environ["USERNAME"],
        password=os.environ["PASSWORD"],
    )
    return ApiClient(configuration=configuration)


def test_info(client):
    api = InfoApi(client)
    api.get_info()
    api.get_metrics()
    api.get_players()
    api.get_settings()


def test_action(client):
    api = ActionApi(client)
    api.post_announce(AnnounceRequest(message="hello"))


def test_ban(client):
    api = ActionApi(client)
    user_id = InfoApi(client).get_players().players[0].user_id

    assert user_id.startswith("steam_")
    # api.post_ban(BanRequest(userId=user_id, message="test"))
    # api.post_unban(UnbanRequest(userId=user_id))

    api.post_ban(BanRequest(userId=user_id))
    api.post_unban(UnbanRequest(userId=user_id))


def test_kick(client):
    api = ActionApi(client)
    user_id = InfoApi(client).get_players().players[0].user_id

    assert user_id.startswith("steam_")
    api.post_kick(KickRequest(userId=user_id, message="test"))
    # api.post_kick(KickRequest(userId=user_id))


def test_shutdown(client):
    api = ActionApi(client)
    api.post_shutdown(ShutdownRequest(waittime=3, message="test"))
    # api.post_shutdown(ShutdownRequest(waittime=3))
