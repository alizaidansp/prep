import requests

def get_request():
    response = requests.get('https://api.thecatapi.com/v1/images/search?limit=10')
    if response.status_code == 200:
        # print(response.json())  # Parsing JSON response
        print(response.json())
    else:
        print(f"Error: {response.status_code}")


def post_request():
    
    # The API endpoint
    url = "https://jsonplaceholder.typicode.com/posts"

    # Data to be sent
    data = {
        "userID": 1,
        "title": "Making a POST request",
        "body": "This is the data we created."
    }

    # A POST request to the API
    response = requests.patch(url, json=data)

    # Print the response
    print(response.json())

try:
    post_request()
except Exception as e:
    print