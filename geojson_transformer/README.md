# GeoJSON Transformer

## Overview
A modular Python tool to convert raw JSON data from social media and other sources (Twitter, Facebook, Instagram, LinkedIn) into standardized GeoJSON format for geospatial analysis.

## Features
- Modular adapters for each data source
- Easily extensible for new sources
- CLI for local JSON file transformation
- Unit tests and CI/CD pipeline included

## Usage
```bash
python cli.py twitter input.json output.geojson
```

## Adding New Sources
Create a new adapter in `adapters/` implementing `BaseAdapter`. Register it in `transformer.py`.

## Development
- Python 3.10+
- Dependencies in `requirements.txt`
- Tests with `pytest`

## License
MIT
