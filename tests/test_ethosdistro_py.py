import aiohttp
import json

from ethosdistro_py import EthosAPI
import pytest
from aioresponses import aioresponses

NOT_ALL_KEYS_PRESENT = "All keys should be in the response"
CONTENT_HEADERS = "text/html"


@pytest.mark.asyncio
async def test_get_panel(get_panel_response):
    """Tests an API call to get block count data for a coin_name"""
    session = aiohttp.ClientSession()
    ethosapi = EthosAPI(session=session)
    assert ethosapi.panel_id_set() is True
    with aioresponses() as m:
        m.get(
            "https://ethereum.miningpoolhub.com/index.php?action=getblockcount&api_key=test&page=api",
            status=200,
            body=json.dumps(get_panel_response),
            headers=CONTENT_HEADERS,
        )

        resp = await ethosapi.async_get_block_count(coin_name=ETHEREUM)
        assert isinstance(resp, int)
        assert resp == 13503059

    await session.close()

