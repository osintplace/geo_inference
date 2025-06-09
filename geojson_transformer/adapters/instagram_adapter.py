from .base_adapter import BaseAdapter

class InstagramAdapter(BaseAdapter):
    def transform(self, raw_json: dict) -> dict:
        # TODO: Implement Instagram specific transformation
        features = []
        # Example placeholder, implement actual extraction
        return {
            "type": "FeatureCollection",
            "features": features
        }
