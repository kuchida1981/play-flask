from http import HTTPStatus


def test_helloworld():
    from app import create_app

    app = create_app()
    client = app.test_client()
    response = client.get("/helloworld")
    assert response.status_code == HTTPStatus.OK
