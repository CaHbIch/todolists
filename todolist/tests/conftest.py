from pytest_factoryboy import register

from tests.factories.factories import UserFactory, BoardFactory, BoardParticipantFactory, GoalCategoryFactory

pytest_plugins = "tests.fixtures"

register(UserFactory)
register(BoardFactory)
register(BoardParticipantFactory)
register(GoalCategoryFactory)
