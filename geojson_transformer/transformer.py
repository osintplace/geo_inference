import json
from adapters import twitter_adapter, facebook_adapter, instagram_adapter, linkedin_adapter

SOURCE_ADAPTERS = {
    "twitter": twitter_adapter.TwitterAdapter(),
    "facebook": facebook_adapter.FacebookAdapter(),
    "instagram": instagram_adapter.InstagramAdapter(),
    "linkedin": linkedin_adapter.LinkedinAdapter(),
}

def transform_to_geojson(source_name: str, raw_json: dict) -> dict:
    adapter = SOURCE_ADAPTERS.get(source_name.lower())
    if not adapter:
        raise ValueError(f"No adapter configured for source '{source_name}'")
    return adapter.transform(raw_json)
