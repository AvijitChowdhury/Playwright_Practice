#documentation how to use api request context in playwright
"""
write the documentation for api request context in playwright

write a full code
def test_api_request_context(playwright):
    # Create a new request context
    request = playwright.request.new_context()
    # Make a GET request to the API endpoint
    response = request.get("https://jsonplaceholder.typicode.com/posts/1")
    # Assert the response status code
    assert response.status == 200
    json_data = response.json()
    print(json_data)
    response.dispose()  # Clean up the request context after the test is done
    


"""