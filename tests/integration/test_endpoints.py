def test_home(client):
    response = client.get("/")
    assert response.status_code == 200


def test_projects(client):
    response = client.get("/projects")
    assert response.status_code == 200


def test_profile(client):
    response = client.get("/profile")
    assert response.status_code == 200
