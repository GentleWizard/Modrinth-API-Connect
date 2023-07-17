"""
This module provides a function for making HTTP GET requests using the `requests` library.
"""

import aiohttp
from ModrinthAPI.Async.utils.Auth_Async import All_Auth


async def request_async(url, params: dict[str, ...] = {}):
    auth = All_Auth
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, params=params, headers=auth, timeout=10) as response:
                response.raise_for_status()
                json_response = await response.text()
                return json_response, response.status
        except aiohttp.ClientError as err:
            return err, response.status
