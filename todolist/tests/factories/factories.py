import factory

from core.models import User
from goals.models import Board
from goals.models import BoardParticipant
from goals.models import Category


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    password = factory.Faker("password")

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        return manager.create_user(*args, **kwargs)


class BoardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Board

    title = factory.Faker("sentence", nb_words=5)


class BoardParticipantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BoardParticipant

    board = factory.SubFactory(BoardFactory)
    user = factory.SubFactory(UserFactory)


class GoalCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    board = factory.SubFactory(BoardFactory)
    title = factory.Faker("sentence", nb_words=3)
    user = factory.SubFactory(UserFactory)