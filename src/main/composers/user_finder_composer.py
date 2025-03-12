from src.infra.db.repositores.user_repositores import UsersRepository
from src.data.use_case.user_finder import UserFinder
from src.presentation.controller.user_finder_controller import UserFinderController


def user_composer_finder():
    repository = UsersRepository()
    use_case = UserFinder(repository)
    controller = UserFinderController(use_case)

    return  controller.handle