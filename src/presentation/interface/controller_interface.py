from abc import ABC, abstractmethod
from src.presentation.http_types.http_requests import HttpRequest
from src.presentation.http_types.http_response import HttpResponse


class ControllerInterface(ABC):

    @abstractmethod
    def handle(self, http_requests: HttpRequest) -> HttpResponse: pass 
