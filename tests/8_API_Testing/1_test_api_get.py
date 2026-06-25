def test_api_get(playwright):
    # Define the API endpoint
    request = playwright.request.new_context() #creates a new request context using the Playwright library, which allows you to make HTTP requests and interact with APIs in your tests.
    # Make a GET request to the API endpoint
    response = request.get("https://jsonplaceholder.typicode.com/posts/1")
    # we can also add headers, query parameters, or authentication details to the request if needed, but in this case, we are making a simple GET request to retrieve a specific post from the JSONPlaceholder API.
    

    # Assert the response status code
    assert response.status == 200 # Verify the response status code, asserting that it is 200 indicates that the request was successful and the server returned the expected response.
    json_data = response.json()
    print(json_data)
    assert json_data["id"] == 1 # using assertion to check that the "id" field in the JSON response is equal to 1, which confirms that the correct post was retrieved from the API., assert actually for validating the correctness of the response data.
    request.dispose() #mean to clean up the request context after the test is done
    print("API GET request test completed successfully.")