
def test_registration_invalid_password_hides_input(client):
    response = client.post(
        "/auth/register",
        json={"username": "alice", "password": "secret!"}
    )

    assert response.status_code == 422
    assert "secret!" not in response.text
