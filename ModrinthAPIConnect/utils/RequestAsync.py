import asyncio
import requests
from ModrinthAPIConnect.Config import return_Auth

Auth = return_Auth()

async def Request(url, params: str = ""):
    try:
        response = await asyncio.wait_for(requests.get(url, params=params, headers=Auth), timeout=10)
        response.raise_for_status()
        return response.json(), response.status_code
    except requests.exceptions.RequestException as err:
        return err, response.status_code