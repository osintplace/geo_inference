import pytest
from adapters.twitter_adapter import TwitterAdapter

def test_transform_with_coordinates():
    adapter = TwitterAdapter()
    raw_json = {
        "posts": [
            {
                "post_id": "1",
                "desc": "Test tweet",
                "create_time": 1234567890,
                "author": {"nickname": "tester"},
                "geo": {"latitude": 51.5074, "longitude": -0.1278}
            }
        ]
    }
    geojson = adapter.transform(raw_json)
    assert geojson["type"] == "FeatureCollection"
    assert len(geojson["features"]) == 1
    feature = geojson["features"][0]
    assert feature["geometry"]["coordinates"] == [-0.1278, 51.5074]
    assert feature["properties"]["post_id"] == "1"
