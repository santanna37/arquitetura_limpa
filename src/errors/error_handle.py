

from src.presentation.http_types.http_response import HttpResponse
from .types import  HttpBadRequest, HttpNotFound


def handle_error(error: Exception) -> HttpResponse:
    if isinstance(error,(HttpBadRequest,HttpNotFound)):
        return HttpResponse(
            status_code = error.status_code,
            body = {
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )
        
    return HttpResponse(
        status_code= 500,
        body = {
            "error": [{
                "title":"Server Error",
                "detail": str(error)
            }]
        }
    )