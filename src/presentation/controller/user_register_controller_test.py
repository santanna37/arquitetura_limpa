from src.presentation.controller.user_register_controller import UserRegisterController
from src.data.test.user_register import UserRegisterSpy




class HttpRequestMock():

    def __init__(self) -> None:
        self.body = { "first_name": "TesteMeu",
                              "last_name" : "register_http",
                              "age": 24
         }


def test_handle_register():
    http_request_mock = HttpRequestMock()
    use_case = UserRegisterSpy()
    user_register_controller = UserRegisterController(use_case)

    response = user_register_controller.handle(http_request_mock)

    print()
    print(response.body)