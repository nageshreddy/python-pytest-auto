import requests


def test_get_posts():
    # URL of the API endpoint
    url = "https://jsonplaceholder.typicode.com/posts"

    # Send a GET request
    response = requests.get(url)

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the response is in JSON format
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    # Assert that the response contains at least one post
    posts = response.json()
    assert len(posts) > 0

    # Assert that the first post contains expected fields
    assert "userId" in posts[0]
    assert "id" in posts[0]
    assert "title" in posts[0]
    assert "body" in posts[0]

