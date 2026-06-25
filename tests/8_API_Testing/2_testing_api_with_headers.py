# for understanding json you should go for json path finder

def test_api_get_with_headers(playwright):
    request = playwright.request.new_context()  # Create a new request context
    response = request.get(
        "https://reqres.in/api/collections/products/records?project_id=32749",
        headers={
            "Accept": "application/json",
            "x-api-key": "pub_449ea5f6ded1d18603a8be371b0ca696d6e08b41b19b766e928914c81c2da2d6",  # Replace with your actual API key
        },
    )
    # Assert the response status code
    assert response.status == 200  # Verify the response status code
    json_data = response.json()
    print(json_data)
            #API key  pub_449ea5f6…
            # Required header x-api-key: x-api-key: pub_449ea5f6ded1d18603a8be371b0ca696d6e08b41b19b766e928914c81c2da2d6
    # for testing the code, write: pytest tests/8_API_Testing/test_api_get.py -s -v