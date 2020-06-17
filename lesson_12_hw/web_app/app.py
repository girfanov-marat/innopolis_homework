"""Application file."""
import asyncio
from typing import Any

from aiohttp import web
from aiohttp.web_request import Request

from lesson_12_hw.web_app.db_async import get_info, insert_or_update
from lesson_12_hw.web_app.utilities import validate_json, validate_input

app = web.Application()


async def status(request: Request) -> Any:
    """
    GET request handler.

    Return list of all entries in db.
    """
    result = await asyncio.shield(get_info())
    return web.Response(text=result)


async def write_data(request: Request) -> Any:
    """
    POST request handler.

    Add data to database if JSON valid.
    """
    res = request.can_read_body
    if res:
        js = await request.json()
    else:
        return web.json_response({"success": "false"})
    if validate_json(js):
        if validate_input(js["identifier"], js["status"]):
            await asyncio.shield(insert_or_update(js["identifier"], js["status"]))
            return web.json_response({"success": "true"})
        else:
            return web.json_response({"success": "false"})
    else:
        return web.json_response({"success": "false"})

routes = [
    ('GET', '/status', status, 'get_info'),
    ('POST', '/add', write_data, 'write_data'),
]

for route in routes:
    app.router.add_route(route[0], route[1], route[2], name=route[3])

if __name__ == '__main__':
    web.run_app(app)
