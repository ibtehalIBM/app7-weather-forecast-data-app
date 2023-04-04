import requests

API_Key = "78f5ee3d03ade6cb0ed8f56622bb6d17"


def get_data(place='tokyo', days=1):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_Key}"
    response = requests.get(url)
    content = response.json()
    filtered_data = content['list']
    nr_values = 8 * days
    filtered_data = filtered_data[:nr_values]

    return filtered_data


if __name__ == '__main__':
    data = get_data('tokyo', 3)
    print(data)
