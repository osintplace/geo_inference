import argparse
import json
from transformer import transform_to_geojson

def main():
    parser = argparse.ArgumentParser(description="Transform source JSON to GeoJSON.")
    parser.add_argument("source", type=str, help="Source name (twitter, facebook, instagram, linkedin)")
    parser.add_argument("input_file", type=str, help="Path to input JSON file")
    parser.add_argument("output_file", type=str, help="Path to output GeoJSON file")

    args = parser.parse_args()

    with open(args.input_file, "r", encoding="utf-8") as f:
        raw_json = json.load(f)

    geojson = transform_to_geojson(args.source, raw_json)

    with open(args.output_file, "w", encoding="utf-8") as f:
        json.dump(geojson, f, indent=2)

    print(f"GeoJSON output saved to {args.output_file}")

if __name__ == "__main__":
    main()
