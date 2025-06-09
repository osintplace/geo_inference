from .base_adapter import BaseAdapter

class TwitterAdapter(BaseAdapter):
    def transform(self, raw_json: dict) -> dict:
        features = []
        for post in raw_json.get("posts", []):
            coords = self._extract_coordinates(post)
            if coords:
                feature = {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": coords
                    },
                    "properties": {
                        "post_id": post.get("post_id"),
                        "text": post.get("desc", ""),
                        "author": post.get("author", {}).get("nickname"),
                        "create_time": post.get("create_time")
                    }
                }
                features.append(feature)

        return {
            "type": "FeatureCollection",
            "features": features
        }

    def _extract_coordinates(self, post):
        geo = post.get("geo")
        if geo and isinstance(geo, dict):
            lat = geo.get("latitude")
            lng = geo.get("longitude")
            if lat is not None and lng is not None:
                return [lng, lat]

        return None
