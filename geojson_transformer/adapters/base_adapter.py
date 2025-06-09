from abc import ABC, abstractmethod

class BaseAdapter(ABC):
    @abstractmethod
    def transform(self, raw_json: dict) -> dict:
        """
        Transform raw source JSON into GeoJSON format.
        """
        pass
