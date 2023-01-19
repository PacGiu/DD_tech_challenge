import requests

# TODO: IP should be read from config
response = requests.post(
    "http://44.201.84.158:/predict",  # no port needed because nginx config within instance
    json={
        "idx": 150000,
        "features": {"attr_a": 1, "attr_b": "c", "scd_a": 0.55, "scd_b": 3},
    },
)


print(response.json()["label"])
