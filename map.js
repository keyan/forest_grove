var geojson;

// Create the map centered in Forest Grove.
var map = L.map('map_canvas').setView([45.528791,-123.126243], 15);

// Default map tiles without overlay.
L.tileLayer(
    'https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        id: 'mapbox.light',
        accessToken: 'pk.eyJ1Ijoia3Bpc2hkYWRpYW4iLCJhIjoiY2pvMTVzN2lwMDdrbTNrcG9mb2RvcDF5aSJ9.wbFcMArvH5wSmVwvRomNmg'
}).addTo(map);

// Add isochrone geojson layer.
geojson = L.geoJson(data, {}).addTo(map);

// Scale bar
L.control.scale().addTo(map)
