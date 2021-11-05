import aiohttp
import json

from ethosdistro_py import EthosAPI
import pytest
from aioresponses import aioresponses

NOT_ALL_KEYS_PRESENT = "All keys should be in the response"
CONTENT_HEADERS = {"Content-Type": "text/html"}


@pytest.mark.asyncio
async def test_get_panel(get_panel_keys, get_panel_response):
    """Tests an API call to get block count data for a panel_id"""
    session = aiohttp.ClientSession()
    ethosapi = EthosAPI(session=session)
    assert ethosapi.panel_id_set() is True
    with aioresponses() as m:
        m.get(
            "http://test.ethosdistro.com/?json=yes",
            status=200,
            body=json.dumps(get_panel_response),
            headers=CONTENT_HEADERS,
        )

        result = await ethosapi.async_get_panel()
        assert isinstance(result, dict)
        assert set(get_panel_keys).issubset(result.keys()), NOT_ALL_KEYS_PRESENT

    await session.close()
