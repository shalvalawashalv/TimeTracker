import pytest



def test_get_activity_invalid_uuid(client):
    response = client.get("/activities/not-a-uuid")
    assert response.status_code == 422


@pytest.mark.parametrize("name", [(""), (" "), ("A"*201),])
def test_create_activity_invalid_name(client, name):
    response = client.post("/activities", json={"name": name})
    assert response.status_code == 422
