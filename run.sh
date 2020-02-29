rm -f data/*

# Generate mapbox calls as curl commands, easy than subprocess.
python3 urls.py
# Allow execution, run, then cleanup.
sudo chmod 777 fetch.sh
./fetch.sh
rm fetch.sh

if ! type "geojson-merge" > /dev/null; then
  npm install -g @mapbox/geojson-merge
fi

geojson-merge data/*.geojson > output/combined.geojson
