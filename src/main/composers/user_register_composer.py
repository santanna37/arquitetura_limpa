from src.infra.db.repositores.user_repositores import UsersRepository
from src.data.use_case.user_register import UserRegister
from src.presentation.controller.user_register_controller import UserRegisterController


def user_composer_register():
    repository = UsersRepository()
    use_case = UserRegister(repository)
    controller = UserRegisterController(use_case)

    return  controller.handle