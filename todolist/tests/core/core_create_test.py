import pytest


@pytest.mark.django_db
def test_create_goal_category(
    user_factory,
    get_auth_client,
    board_participant_factory,
    goal_category_factory,
):
    user = user_factory(username="Skypro", password="test12345")
    auth_client = get_auth_client(user)
    board_participant = board_participant_factory(
        board__title="test board", user=user
    )

    expected_response = {
        "title": "test cat",
        "is_deleted": False,
        "board": board_participant.board.id,
    }

    data = {
        "board": board_participant.board.id,
        "title": "test cat",
    }

    response = auth_client.post(
        "/goals/goal_category/create",
        data=data,
        content_type="application/json",
    )

    print(response.data)

    assert response.status_code == 201
    id_ = response.data.pop("id")
    created = response.data.pop("created")
    updated = response.data.pop("updated")
    assert (
        response.data == expected_response
        and isinstance(id_, int)
        and isinstance(created, str)
        and isinstance(updated, str)
        and created == updated
    )