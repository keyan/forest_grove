# Forest Grove Oregon, park walking isochrone map
Notes and scripts to simplify generation of GeoJSON isochrone walking maps around existing parks in Forest Grove Oregon.

## Usage
To produce a merged GeoJSON for the default locations:
```
./run.sh
```

Optionally I have included the [mapstarter](https://github.com/veltman/mapstarter) project as a submodule which makes it easy to drag/drop GeoJSON and convert to SVG for import into Adobe Illustrator or similar flat graphic editing tools. To use `mapstarter`:
```
cd mapstarter
npm install .
open www/index.html
```

## Documentation
https://docs.mapbox.com/api/navigation/#isochrone

Example output in `/output` or:
https://gist.github.com/keyan/9e9878ab8882442ec192c0ae8945af1c
