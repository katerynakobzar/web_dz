import requests
from unittest.mock import patch

def get_weather(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Error {response.status_code}"}

def test_get_weather():
    mock_response = {
        "weather": [{"description": "clear sky"}],
        "main": {"temp": 293.15},
        "name": "Kyiv",
    }

    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        city_name = "Kyiv"
        api_key = "test_api_key"
        result = get_weather(city_name, api_key)

        assert result["weather"][0]["description"] == "clear sky"
        assert result["main"]["temp"] == 293.15
        assert result["name"] == "Kyiv"

        mock_get.assert_called_once_with(
            f"http://api.openweathermap.org/data/2.5/weather?q=Kyiv&appid=test_api_key"
        )


if __name__ == "__main__":
    test_get_weather()
    print("Тест функції get_weather успішно пройдено!")