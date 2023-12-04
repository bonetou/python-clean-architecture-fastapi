def test_it_should_return_200_when_health_check_succeeds(test_client):
    response = test_client.get("/management/health-check")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}
