import requests


def get_medicine(medicine_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{medicine_id}"

    response = send_request("GET", url)

    data = response.json()

    return data


def send_request(method, url):
    response = requests.request(method, url, timeout=10)

    response.raise_for_status()
    return response


def validate_medicine_id(medicine_id):

    try:
        medicine_id = int(medicine_id)
    except ValueError:
        raise ValueError("Medicine ID must be a whole number.")

    if medicine_id <= 0:
        raise ValueError("Medicine ID must be greater than zero.")

    return medicine_id
