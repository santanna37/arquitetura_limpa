from flask import request as FlaskRequest
from typing import Callable
from src.presentation.http_types.http_requests import HttpRequest
from src.presentation.http_types.http_response import HttpResponse


def request_adapter(requests: FlaskRequest, controller: Callable) ->HttpResponse:

    body = None
    if requests.data: body = requests.json

    http_request = HttpRequest(
        headers = requests.headers,
        body = body,
        query_params= requests.args,
        url= requests.full_path,
        path_params= requests.view_args

    )


    http_response = controller(http_request)

    return http_response