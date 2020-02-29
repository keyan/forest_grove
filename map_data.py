import json


def write_js_data(input_file, output_file):
    with open(input_file, 'r') as f:
        geojson = json.load(f)

    with open(output_file, 'w') as f:
        f.write(f'var data = ')
        f.write(json.dumps(geojson))

write_js_data(
    'output/combined.geojson',
    'output/combined.js',
)
